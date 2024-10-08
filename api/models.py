# encoding: utf-8
from django.db import models
from django.contrib.auth.models import (
        AbstractBaseUser, BaseUserManager, PermissionsMixin)
import uuid
from backend import settings

ADMIN = 'admin'
SUPERADMIN = 'superadmin'
APPRENANT = 'apprenant'
USER_TYPES = (
    (ADMIN, ADMIN),
    (SUPERADMIN, SUPERADMIN),
    (APPRENANT, APPRENANT)
)

BEGINNER = 'beginner'
INTERMEDIATE = 'intermediate'
ADVANCED = 'Advanced'
LEVEL_TYPE = (
    (BEGINNER, BEGINNER),
    (INTERMEDIATE, INTERMEDIATE),
    (ADVANCED, ADVANCED)
)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('user_type', SUPERADMIN)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    slug = models.SlugField(default=uuid.uuid1, editable=False)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    address = models.TextField(null=True, blank=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPES)
    is_active = models.BooleanField(('active'), default=True)
    is_staff = models.BooleanField(default=False)
    password_reset_count = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True,default=0)
    first_connexion = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()


    USERNAME_FIELD = 'email'
    # these field are required on registering
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')
        app_label = "api"

    def __str__(self):
        return f'<User: {self.pk}, email: {self.email}, user_type: {self.user_type}>'


class Course(models.Model):
    slug = models.SlugField(default=uuid.uuid1, editable=False)
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    level = models.CharField(max_length=50, choices=LEVEL_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'<Course: {self.pk}, title: {self.title}>'
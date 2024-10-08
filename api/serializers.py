from rest_framework.serializers import ModelSerializer
from api.models import User, Course, APPRENANT
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.core.exceptions import ValidationError

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('user_permissions', 'groups', 'is_superuser', 'is_staff')


class UserGetSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('user_permissions', 'groups', 'is_superuser', 'is_staff', 'password')


class UserRegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        exclude = (
            'user_permissions', 'groups', 'is_superuser', 'is_staff')
        
    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.user_type = APPRENANT
        user.save()
        return user


class LoginSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password')


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
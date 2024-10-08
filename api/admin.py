# encoding: utf-8

from django.contrib import admin

# Register your models here.
# Import our models module.
from api.models import User, Course


admin.site.register(User)
admin.site.register(Course)
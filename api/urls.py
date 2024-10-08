from django.urls import re_path
from api import views
from rest_framework_jwt.views import (obtain_jwt_token, refresh_jwt_token,
                                      verify_jwt_token)

urlpatterns = [

  re_path(r'^auth/get-token', obtain_jwt_token),
  re_path(r'^auth/verify-token', verify_jwt_token),
  re_path(r'^auth/refresh-token', refresh_jwt_token),
  re_path(r'^auth/register/$', views.RegisterUser.as_view()),
  re_path(r'^auth/login/$', views.LoginView.as_view()),
  re_path(r'^user/(?P<id>\d+)/$', views.UserAPIView.as_view()),
  
#   Courses Endpoint Crud
  re_path(r'^courses/$', views.CourseAPIListView.as_view()),
  re_path(r'^courses/(?P<id>\d+)/$', views.CourseAPIView.as_view()),
]

from http.client import HTTPResponse
from rest_framework.response import Response
from api.serializers import (LoginSerializer, UserSerializer, UserGetSerializer,
                             UserRegisterSerializer, CourseSerializer)
from api.models import User, Course, ADMIN, APPRENANT
from rest_framework import generics
from backend import settings
from django.utils import timezone
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class RegisterUser( generics.CreateAPIView):
    permission_classes = (
        
    )
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    
    def post(self, request, format=None):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            item=User.objects.get(id=serializer.data['id'])
            item.save()
            return Response(UserGetSerializer(item).data)
        return Response(serializer.errors, status=404)


class LoginView(generics.CreateAPIView):
    permission_classes = (

    )
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        if 'email' in request.data and request.data['email']:
            if 'password' in request.data and request.data['password']:
                try:
                    email = request.data['email'] 
                    print(email)
                    search_item = User.objects.filter(email__iexact=email)
                    if search_item.exists():
                        item = search_item.last()
                        if item and item.email != email:
                            email = item.email
                            request.data['email'] = email
                    item = User.objects.get(email=email)
                    user = authenticate(request, email=email,
                                        password=request.data['password'])
                    if user and not item.is_active:
                        return Response({
                            "status": "failure",
                            "message": "This account is inactive"},
                            status=401)
                    elif user and user.is_active:
                        token = jwt_encode_handler(jwt_payload_handler(user))
                        return Response({
                            'token': token,
                            'data': UserGetSerializer(user).data
                        }, status=200)
                    else:
                        return Response({
                            "message": "Incorrect credetials"},
                                        status=400)
                except User.DoesNotExist:
                    return Response({
                        "status": "failure",
                        "message": "This account does not exist"}, status=400)
            return Response({"message": "Password required"}, status=401)
        return Response({"message": "Email required"}, status=401)


class UserAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, id, format=None):
        if request.user.is_superuser or request.user.user_type==ADMIN:
            try:
                item = User.objects.get(id=id)
                serializer = UserGetSerializer(item)
                response = Response(serializer.data)
                return response
            except User.DoesNotExist:
                return Response(status=404)
        else:
            return Response({"message": "Unauthorized action"})

    def put(self, request, id, format=None):
        try:
            item = User.objects.get(id=id)
            self.data = request.data.copy()
            if 'password' in request.data:
                item.set_password(request.data['password'])
                self.data['password'] = item.password
            serializer = UserSerializer(item, data=self.data, partial=True)
            if serializer.is_valid():
                item = serializer.save()
                response = Response(UserGetSerializer(item).data)
                return response
            return Response(serializer.errors, status=400)
        except User.DoesNotExist:
            return Response(status=404)

    def delete(self, request, id, format=None):
        try:
            item = User.objects.get(id=id)
            if request.user.is_superuser or request.user.user_type == ADMIN:
                item.delete()
                return Response(status=204)
            return Response({"message": "Unauthorized action"}, status=401)
        except User.DoesNotExist:
            return Response(status=404)


class UserAPIListView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, format=None):
        if request.user.is_superuser or request.user.user_type == ADMIN:
            items = User.objects.filter(user_type=APPRENANT)
            return Response(UserGetSerializer(items, many=True).data)
        else:
            return Response({"message": "Unauthorized action"})


class CourseAPIListView(generics.CreateAPIView):
    permission_classes = ()
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, format=None):
        items = Course.objects.order_by('-pk')
        return Response(CourseSerializer(items, many=True).data)

    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CourseAPIView(generics.RetrieveAPIView):
    permission_classes = ()
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, id, format=None):
        try:
            item = Course.objects.get(id=id)
            return Response(CourseSerializer(item).data)
        except Course.DoesNotExist:
            return Response(status=404)
    
    def put(self, request, id, format=None):
        try:
            item = Course.objects.get(id=id)
        except Course.DoesNotExist:
            return Response(status=404)
        serializer = CourseSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(CourseSerializer(item).data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Course.objects.get(id=id)
        except Course.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204) 
    

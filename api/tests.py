# from PIL import Image as PILImage
from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from api.models import *
API_URL = '/api'


class GetTokenApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = get_user_model().objects.create_user(
         'yello_app@yopmail.com', 'P@sser123')
        self.client.force_authenticate(self.user)

    def test_get_token(self):
        data = {'email': 'yello_app@yopmail.com', 'password': 'P@sser123'}
        res = self.client.post(API_URL+'/auth/get-token', data)
        self.assertEqual(res.status_code, 200)

    def test_verify_token(self):
        data = {'email': 'yello_app@yopmail.com', 'password': 'P@sser123'}
        res1 = self.client.post(API_URL+'/auth/get-token', data)
        res = self.client.post(
            API_URL+'/auth/verify-token',
            {'token': res1.json()['token']})
        self.assertEqual(res.status_code, 200)

    def test_refresh_token(self):
        data = {'email': 'yello_app@yopmail.com',
                'password': 'P@sser123'}
        res1 = self.client.post(API_URL+'/auth/get-token', data)
        res = self.client.post(API_URL+'/auth/refresh-token',
                               {'token': res1.json()['token']})
        self.assertEqual(res.status_code, 200)

    def test_login(self):
        data = {'email': 'yello_app@yopmail.com', 'password': 'P@sser123'}
        res = self.client.post(API_URL+'/auth/login/', data)
        self.assertEqual(res.status_code, 200)


class RegisterUserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'yello_app@yopmail.com', 'P@sser123')
        self.client.force_authenticate(self.user)

        self.data = {'first_name': 'Cherif', 'last_name': 'Guisse',
                     'email': 'guissemohamedcherif@gmail.com', 'password': 'GuisseDev@1',
                     'user_type': 'apprenant'}

    def test_register_user(self):
        res = self.client.post(API_URL+'/auth/register/', self.data)
        self.assertEqual(res.status_code, 200)


class CourseCRUDApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user('yello_app@yopmail.com', 'P@sser123')

        self.data = {
            'title': 'Django Course',
            'description': "It's a course about django rest framework",
            'level': 'beginner'
            }
        self.data1 = {
            'title': 'Node Course',
            'description': "It's a course about node Js Express",
            'level': 'advanced'
            }
        self.client.force_authenticate(self.user)

    def test_create_course(self):
        res = self.client.post(API_URL+'/courses/', self.data)
        self.assertEqual(res.status_code, 201)

    def test_get_courses_list(self):
        self.client.post(API_URL+'/courses/', self.data)
        self.client.post(API_URL+'/courses/', self.data1)
        res = self.client.get(API_URL+'/courses/')
        self.assertEqual(res.status_code, 200)

    def test_update_course(self):
        res1 = self.client.post(API_URL+'/courses/', self.data)
        data1 = {'title': 'Updated Course'}
        res = self.client.put(API_URL+'/courses/'+str(res1.json()['id']) + '/', data1)
        self.assertEqual(res.status_code, 200)

    def test_delete_course(self):
        res1 = self.client.post(API_URL+'/courses/', self.data)
        res = self.client.delete(API_URL+'/courses/'+str(res1.json()['id']) + '/')
        self.assertEqual(res.status_code, 204)

# myproject/users/tests.py

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_registration_and_token(self):
        # Register a new user
        response = self.client.post(reverse('user-register'), {
            'email': 'test@example.com',
            'password': 'StrongPassword123'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Obtain token
        response = self.client.post(reverse('token_obtain_pair'), {
            'email': 'test@example.com',
            'password': 'StrongPassword123'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        access_token = response.data['access']

        # Access protected endpoint
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = self.client.get(reverse('user-me'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@example.com')

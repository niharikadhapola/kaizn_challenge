from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import CustomUser

class RegisterUserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user_success(self):
        data = {
            "username": "testuser2",
            "email": "test@example.com",
            "password": "testpassword"
        }
        response = self.client.post('/api/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CustomUser.objects.filter(username='testuser').exists())

    def test_register_user_invalid_data(self):
        data = {
            "username": "testuser",
            "email": "invalid_email",  # Invalid email format
            "password": "testpassword"
        }
        response = self.client.post('/api/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
class UserLoginAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_user_login_success(self):
        data = {
            "username": "testuser2",
            "password": "testpassword"
        }
        response = self.client.post('/api/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_user_login_invalid_credentials(self):
        data = {
            "username": "testuser",
            "password": "invalid_password"
        }
        response = self.client.post('/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

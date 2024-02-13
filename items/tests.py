from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Item

class ItemListAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_item_list_view_with_authentication(self):
        # Assuming you have a user object to authenticate with
        user = Item.objects.create_user(username='testuser', password='testpassword')

        # Authenticating the client
        self.client.force_authenticate(user=user)

        # Making a GET request to the item list endpoint
        response = self.client.get('/api/items/')

        # Asserting that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_item_list_view_without_authentication(self):
        # Making a GET request to the item list endpoint without authentication
        response = self.client.get('/api/items/')

        # Asserting that the response status code is 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ItemCreateAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_item_create_view_with_authentication(self):
        # Assuming you have a user object to authenticate with
        user = Item.objects.create_user(username='testuser', password='testpassword')

        # Authenticating the client
        self.client.force_authenticate(user=user)

        # Data for creating an item
        data = {
            "name": "Test Item",
            "category": "Test Category",
            "tags": ["tag1", "tag2"],
            "in_stock": True,
            "available_stock": 10,
            "stock_status": "In stock"
        }

        # Making a POST request to the item create endpoint
        response = self.client.post('/api/items/', data, format='json')

        # Asserting that the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_item_create_view_without_authentication(self):
        # Data for creating an item
        data = {
            "name": "Test Item",
            "category": "Test Category",
            "tags": ["tag1", "tag2"],
            "in_stock": True,
            "available_stock": 10,
            "stock_status": "In stock"
        }

        # Making a POST request to the item create endpoint without authentication
        response = self.client.post('/api/items/', data, format='json')

        # Asserting that the response status code is 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

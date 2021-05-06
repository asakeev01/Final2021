from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse
from .models import Category

class CategoryTest(APITestCase):
    def setUp(self):
        category = Category.objects.create(title = 'Pants')
        category.save()
    def test_get_category_detail(self):
        category = Category.objects.first()
        url = category.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



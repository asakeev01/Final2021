from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse
from django.contrib.auth.models import User
from .models import Bookmark

class TestUser(APITestCase):
    def setUp(self):
        user = User.objects.create(username = 'aidar', email = 'aidar@mail.ru')
        user.set_password('Aidar')
        user.save()
    def test_get_user_list(self):
        self.client.login(username = 'aidar', password = 'Aidar')
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_get_user_detail(self):
        self.client.login(username = 'aidar', password = 'Aidar')
        user = User.objects.first()
        url = reverse('user-detail', kwargs = {'pk': user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_create_user(self):
        url = reverse('user-create')
        data = {'username' : 'admin', 'email' : 'admin@mail.ru', 'password1' : 'Aidar', 'password2' : 'Aidar'}
        response = self.client.post(url, data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_get_bookmark_detail(self):
        self.client.login(username = 'aidar', password = 'Aidar')
        user = User.objects.first()
        url = reverse('bookmark-detail', kwargs = {'pk': user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product, ProductItem


class ProductTest(APITestCase):
    def setUp(self):
        product = Product.objects.create(name = 'Jeans', description = 'Long_stylish')
        product_item = ProductItem.objects.create(color = 'Blue', size = 40, quantity = 3, price = 1000, product = product) 
        user = User.objects.create(username = 'super', email = 'super@mail.ru')
        user.set_password('none')
        user.save()  
        self.client.login(username = 'super', password = 'none')
    def test_get_product_list(self):
        url = reverse('product-list')
        responce = self.client.get(url)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
    def test_get_product_detail(self):
        product = Product.objects.first()
        url = product.get_absolute_url()
        responce = self.client.get(url)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
    def test_get_product_item_detail(self):
        product_item = ProductItem.objects.first()
        url = product_item.get_absolute_url()
        responce = self.client.get(url)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
    def test_add_product_item_to_bookmark(self):
        product_item = ProductItem.objects.first()
        url = product_item.add_to_bookmark_url()
        responce = self.client.post(url)
        self.assertEqual(responce.status_code, status.HTTP_202_ACCEPTED)
    def test_remove_product_item_from_bookmark(self):
        product_item = ProductItem.objects.first()
        url = product_item.add_to_bookmark_url()
        responce = self.client.post(url)
        responce = self.client.post(url)
        self.assertEqual(responce.status_code, status.HTTP_202_ACCEPTED)


        

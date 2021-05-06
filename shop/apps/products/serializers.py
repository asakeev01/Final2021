from rest_framework import serializers
from .models import Product, ProductItem, ProductItemImage


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('url', 'name', 'description', 'categories')


class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
    product_items = ProductItem.instock.all()

    class Meta:
        model = Product
        fields = ('name', 'description', 'product_items', 'categories')


class ProductItemSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductItem
        fields = ('url', 'color', 'size', 'quantity', 'price', 'product', 'product_item_images')


class ProductImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductItemImage
        fields = ('product_item', 'image',)
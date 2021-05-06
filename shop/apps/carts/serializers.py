from rest_framework import serializers

from apps.products.serializers import ProductItemSerializer
from .models import Cart, CartItem


class CartSerializer(serializers.HyperlinkedModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ('user', 'cart_items', 'total')

    def get_total(self, obj):
        summa = 0
        for item in obj.cart_items.all():
            product_item = item.product_item
            summa += product_item.price * item.amount
        return summa


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ('amount', 'product_item')

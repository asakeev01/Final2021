from rest_framework import generics
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.response import Response
from rest_framework import status
from apps.products.models import ProductItem


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartItemView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def post(self, request, *args, **kwargs):
        cart = request.user.cart
        cartitems = cart.cart_items.all()
        product_item = ProductItem.objects.get(pk=request.data['product_item'])
        for item in cartitems:
            if item.product_item == product_item:
                return Response(data={'message': 'The product is already in the cart'}, status=status.HTTP_400_BAD_REQUEST)
            if product_item.quantity == 0 or int(request.data['amount']) > product_item.quantity:
                return Response(data={'message': 'No enough quantity'}, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)


    def perform_create(self, serializer):
        serializer.save(cart=self.request.user.cart)
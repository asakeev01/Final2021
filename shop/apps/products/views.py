from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductItemListView(generics.ListAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer


class ProductItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductItem.instock.all()
    serializer_class = ProductItemSerializer


class ProductImageView(generics.RetrieveAPIView):
    queryset = ProductItemImage.objects.all()
    serializer_class = ProductImageSerializer


@api_view(['POST'])
def add_to_bookmark(request, pk):
    product = ProductItem.objects.get(pk=pk)
    bookmark = request.user.bookmark
    if product not in bookmark.product_items.all():
        bookmark.product_items.add(product)
        return Response(status=status.HTTP_202_ACCEPTED, data={'message': 'successfully added to bookmarks'})
    else:
        bookmark.product_items.remove(product)
        return Response(status=status.HTTP_202_ACCEPTED, data={'message': 'successfully removed from bookmarks'})





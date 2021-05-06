from rest_framework import generics
from .models import Order, Delivery
from .serializers import OrderSerializer, DeliverySerializer


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(
            user=user,
            cart=user.cart,
            # total=user.cart.total
        )

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



class DeliveryDetailView(generics.RetrieveAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
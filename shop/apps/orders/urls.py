
from django.urls import path
from . import views


urlpatterns = [
    path('', views.OrderListCreateView.as_view(), name='order-list-create'),
    path('deliveries/<int:pk>/', views.DeliveryDetailView.as_view(), name='delivery-detail'),
    path('<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
]
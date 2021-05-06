
from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.CartDetailView.as_view(), name='cart-detail'),
    path('cartitem/create/', views.CartItemView.as_view(), name='cartitem-create'),
    path('cartitem/<int:pk>/', views.CartItemDetailView.as_view(), name='cartitem-detail')
]

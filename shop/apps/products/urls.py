
from django.urls import path
from . import views
from apps.carts.views import CartItemView


urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/items/', views.ProductItemListView.as_view(), name='product-items-list'),
    path('items/<int:pk>/', views.ProductItemDetailView.as_view(), name='productitem-detail'),
    path('items/<int:pk>/bookmark/', views.add_to_bookmark, name='add-to-bookmark'),
    path('item/image/<int:pk>/', views.ProductImageView.as_view(), name='productitemimage-detail'),
    path('items/<int:pk>/cart/', CartItemView.as_view(), name='add-to-cart'),
]
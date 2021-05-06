from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.categories.views import CategoryViewSet


router = DefaultRouter()
router.register(r'', CategoryViewSet)


urlpatterns = []

urlpatterns += router.urls
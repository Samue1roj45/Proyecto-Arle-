from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import CarritoViewSet

router = DefaultRouter()
router.register(r'carrito', CarritoViewSet, basename='carrito')

urlpatterns = router.urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InmuebleViewSet, FavoritoViewSet


router = DefaultRouter()
router.register(r'inmuebles', InmuebleViewSet)
router.register(r'favoritos', FavoritoViewSet, basename='favoritos')

urlpatterns = [
    path('', include(router.urls)),
]
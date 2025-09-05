from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropietarioViewSet, InmuebleViewSet, FavoritoViewSet
from django.urls import path

# Configuramos un router para REST Framework
# Esto generará automáticamente las rutas CRUD para nuestros modelos
router = DefaultRouter()
router.register(r'propietarios', PropietarioViewSet)
router.register(r'inmuebles', InmuebleViewSet)
router.register(r'favoritos', FavoritoViewSet)

urlpatterns = [
    # Incluimos todas las URLs generadas por el router
    path('', include(router.urls)),
]
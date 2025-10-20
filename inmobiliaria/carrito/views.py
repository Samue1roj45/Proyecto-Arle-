from rest_framework import viewsets, permissions
from .models import Carrito
from .serializers import CarritoSerializer

class CarritoViewSet(viewsets.ModelViewSet):
    serializer_class = CarritoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Solo muestra los inmuebles del carrito del usuario autenticado
        return Carrito.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        # Guarda el carrito con el usuario actual
        serializer.save(usuario=self.request.user)

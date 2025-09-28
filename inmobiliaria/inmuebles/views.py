from .models import Inmueble
from .serializers import InmuebleSerializer
from rest_framework import viewsets, permissions
from .models import Favorito
from .serializers import FavoritoSerializer

class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorito.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class InmuebleViewSet(viewsets.ModelViewSet):
    queryset = Inmueble.objects.all()
    serializer_class = InmuebleSerializer

    def create(self, request, *args, **kwargs):
        print("Datos recibidos:", request.data)  # <-- mira la consola
        return super().create(request, *args, **kwargs)
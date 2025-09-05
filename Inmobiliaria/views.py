from rest_framework import viewsets, permissions
from .models import Propietario, Inmueble, Favorito
from .serializers import PropietarioSerializer, InmuebleSerializer, FavoritoSerializer
#mostrar inmuebles en un html
from django.shortcuts import render,get_object_or_404
from .models import Inmueble

def detalle_inmueble(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    return render(request, "inmuebles/detalle.html", {"inmueble": inmueble})

def lista_inmuebles(request):
    inmuebles = Inmueble.objects.all().order_by('-fecha_publicacion')
    return render(request, "inmuebles/lista.html", {"inmuebles": inmuebles})


class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer
    permission_classes = [permissions.AllowAny]


class InmuebleViewSet(viewsets.ModelViewSet):
    queryset = Inmueble.objects.all().order_by('-fecha_publicacion')
    serializer_class = InmuebleSerializer
    permission_classes = [permissions.AllowAny]


class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorito.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
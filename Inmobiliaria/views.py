from rest_framework import viewsets, permissions
from .models import Propietario, Inmueble, Favorito
from .serializers import PropietarioSerializer, InmuebleSerializer, FavoritoSerializer
#mostrar inmuebles en un html
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def agregar_favorito(request, inmueble_id):
    inmueble = Inmueble.objects.get(id=inmueble_id)
    Favorito.objects.get_or_create(usuario=request.user, inmueble=inmueble)
    return redirect("lista_inmuebles")

@login_required
def eliminar_favorito(request, inmueble_id):
    Favorito.objects.filter(usuario=request.user, inmueble_id=inmueble_id).delete()
    return redirect("lista_inmuebles")


def detalle_inmueble(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    return render(request, "inmuebles/detalle.html", {"inmueble": inmueble})

def lista_inmuebles(request):
    inmuebles = Inmueble.objects.all()
    favoritos_ids = Favorito.objects.filter(usuario=request.user).values_list("inmueble_id", flat=True)
    return render(request, "inmuebles/lista.html", {
        "inmuebles": inmuebles,
        "favoritos_ids": favoritos_ids,
    })


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
from rest_framework import serializers
from .models import Propietario, Inmueble, Favorito

class PropietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propietario
        fields = '__all__'


class InmuebleSerializer(serializers.ModelSerializer):
    propietario = serializers.PrimaryKeyRelatedField(queryset=Propietario.objects.all())

    class Meta:
        model = Inmueble
        fields = [
            'id', 'titulo', 'tipo', 'ciudad', 'estado', 'direccion',
            'precio', 'habitaciones', 'banos', 'area_sqft',
            'imagen', 'fecha_publicacion', 'disponible', 'propietario'
        ]


class FavoritoSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField(read_only=True)  # username
    inmueble = InmuebleSerializer(read_only=True)

    class Meta:
        model = Favorito
        fields = ['id', 'usuario', 'inmueble', 'fecha_guardado']
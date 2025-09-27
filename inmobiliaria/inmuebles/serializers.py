from rest_framework import serializers
from .models import Inmueble
from .models import Favorito


class InmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmueble
        fields = '__all__'

class FavoritoSerializer(serializers.ModelSerializer):
    inmueble = InmuebleSerializer(read_only=True)  # devuelve el objeto completo
    inmueble_id = serializers.PrimaryKeyRelatedField(
        queryset=Inmueble.objects.all(),
        source='inmueble',
        write_only=True
    )
    class Meta:
        model = Favorito
        fields = ['id', 'inmueble', 'inmueble_id', 'fecha_agregado']
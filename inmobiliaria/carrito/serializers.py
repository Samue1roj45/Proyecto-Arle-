from rest_framework import serializers
from .models import Carrito
from inmuebles.models import Inmueble
from inmuebles.serializers import InmuebleSerializer

class CarritoSerializer(serializers.ModelSerializer):
    inmueble = InmuebleSerializer(read_only=True)
    inmueble_id = serializers.PrimaryKeyRelatedField(
        queryset=Inmueble.objects.all(),
        source='inmueble',
        write_only=True
    )

    class Meta:
        model = Carrito
        fields = ['id', 'inmueble', 'inmueble_id', 'fecha_agregado']
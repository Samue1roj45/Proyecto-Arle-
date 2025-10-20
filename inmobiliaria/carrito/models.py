from django.db import models
from django.contrib.auth.models import User
from inmuebles.models import Inmueble

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carrito')
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='en_carrito')
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.inmueble.descripcion} en el carrito de {self.usuario.username}"

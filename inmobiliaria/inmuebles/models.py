from django.db import models
from django.contrib.auth.models import User

class Inmueble(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    metros = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, blank=True, null=True)
    codigo_postal = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(max_length=50, choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Condo', 'Condo')])
    status = models.CharField(max_length=50, choices=[('Available', 'Available'), ('Sold', 'Sold'), ('Rented', 'Rented')])
    imagen = models.ImageField(upload_to="inmuebles/", blank=True, null=True)

    def __str__(self):
        return self.titulo

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favoritos")
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name="favoritos")
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("usuario", "inmueble")  # evita duplicados

    def __str__(self):
        return f"{self.usuario.username} -> {self.inmueble.id}"
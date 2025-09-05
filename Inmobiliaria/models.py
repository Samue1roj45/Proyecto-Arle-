from django.db import models
from django.contrib.auth.models import User  # Para manejar usuarios (clientes que marcan favoritos)

class Propietario(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Inmueble(models.Model):
    TIPOS_INMUEBLE = [
        ('AP', 'Apartamento'),
        ('CA', 'Casa'),
        ('CO', 'Condominio'),
        ('TO', 'Townhouse'),
    ]

    titulo = models.CharField(max_length=200)  # Ej: "Casa moderna con piscina"
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='inmuebles')
    tipo = models.CharField(max_length=2, choices=TIPOS_INMUEBLE)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    direccion = models.CharField(max_length=250)

    precio = models.DecimalField(max_digits=12, decimal_places=2)
    habitaciones = models.PositiveIntegerField()
    banos = models.PositiveIntegerField()
    area_sqft = models.PositiveIntegerField(help_text="Área en pies cuadrados")

    imagen = models.ImageField(upload_to='inmuebles/', blank=True, null=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} - {self.ciudad}, {self.estado}"


class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favoritos")
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name="favoritos")
    fecha_guardado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'inmueble')  # Un usuario no puede guardar el mismo inmueble dos veces

    def __str__(self):
        return f"{self.usuario.username} → {self.inmueble.titulo}"
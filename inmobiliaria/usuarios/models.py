from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    foto = models.ImageField(upload_to="usuarios/", blank=True, null=True)

    def __str__(self):
        return self.user.username
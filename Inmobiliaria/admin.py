from django.contrib import admin
from .models import Propietario, Inmueble, Favorito

admin.site.register(Propietario)
admin.site.register(Inmueble)
admin.site.register(Favorito)

# Register your models here.
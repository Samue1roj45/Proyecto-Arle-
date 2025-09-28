from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from django.db.models import Count
from django.utils.html import format_html

# Importar modelos de auth
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

# Importar modelos
from .models import Inmueble, Favorito


# ---- Custom AdminSite ----
class CustomAdminSite(admin.AdminSite):
    site_header = "Panel de Administración - HomeFinder"
    site_title = "HomeFinder Admin"
    index_title = "Bienvenido al Panel de Control"

    def get_app_list(self, request):
        """
        Renombrar la sección de usuarios y mantener apps organizadas.
        """
        app_list = super().get_app_list(request)
        for app in app_list:
            if app["app_label"] == "auth":
                app["name"] = "Gestión de usuarios"
        return app_list

    def index(self, request, extra_context=None):
        """
        Sobrescribimos la vista principal del admin para mostrar el dashboard.
        """
        # Métricas de inmuebles
        total_inmuebles = Inmueble.objects.count()
        disponibles = Inmueble.objects.filter(status="Available").count()
        vendidos = Inmueble.objects.filter(status="Sold").count()
        rentados = Inmueble.objects.filter(status="Rented").count()

        # Métricas de favoritos
        total_favoritos = Favorito.objects.count()
        top_inmuebles = (
            Inmueble.objects.annotate(num_favoritos=Count("favoritos"))
            .order_by("-num_favoritos")[:5]
        )
        # Inmueble más agregado a favoritos
        favorito_top = (
            Inmueble.objects
            .annotate(num_favs=Count('favoritos'))
            .order_by('-num_favs')
            .first()
        )

        context = {
            **self.each_context(request),
            "total_inmuebles": total_inmuebles,
            "disponibles": disponibles,
            "vendidos": vendidos,
            "rentados": rentados,
            "total_favoritos": total_favoritos,
            "top_inmuebles": top_inmuebles,
            "favorito_top": favorito_top,
        }
        return TemplateResponse(request, "admin/dashboard.html", context)


# Instancia del admin personalizado
custom_admin_site = CustomAdminSite(name="custom_admin")


# ---- Admin para Inmueble ----
@admin.register(Inmueble, site=custom_admin_site)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "precio", "ciudad", "status")
    search_fields = ("titulo", "ciudad", "estado")
    list_filter = ("status", "tipo", "ciudad")

    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" width="80" style="border-radius:8px;" />', obj.imagen.url
            )
        return "Sin imagen"
    mostrar_imagen.short_description = "Imagen"


# ---- Admin para Favorito ----
@admin.register(Favorito, site=custom_admin_site)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "inmueble", "fecha_agregado")
    search_fields = ("usuario__username", "inmueble__titulo")
    list_filter = ("fecha_agregado",)


# ---- Registrar usuarios y grupos ----
custom_admin_site.register(User, UserAdmin)
custom_admin_site.register(Group, GroupAdmin)
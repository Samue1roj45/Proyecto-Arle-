from django.urls import path
from .views import UserCreateView

urlpatterns = [
    path("usuarios/", UserCreateView.as_view(), name="user-register"),
]
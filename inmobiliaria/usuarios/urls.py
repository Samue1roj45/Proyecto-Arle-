from django.urls import path
from .views import UserCreateView, UserDetailView

urlpatterns = [
    path("usuarios/", UserCreateView.as_view(), name="user-register"),
    path("me/", UserDetailView.as_view(), name="user-detail"),
]
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PerfilUsuario


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = ["foto"]


class UserSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer(required=False)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "first_name", "last_name", "perfil"]
        extra_kwargs = {
            "username": {"required": False},
            "email": {"required": False},
        }

    def create(self, validated_data):
        perfil_data = validated_data.pop("perfil", {})
        password = validated_data.pop("password", None)

        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)
        user.save()

        # Actualiza el perfil creado automáticamente (por signal)
        perfil = getattr(user, "perfil", None)
        if perfil_data and perfil:
            for attr, value in perfil_data.items():
                setattr(perfil, attr, value)
            perfil.save()

        return user

    def update(self, instance, validated_data):
        perfil_data = validated_data.pop("perfil", {})
        perfil = getattr(instance, "perfil", None)

        # Actualiza campos del usuario
        for attr, value in validated_data.items():
            if attr == "password":
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()

        # Actualiza campos del perfil (si existe)
        if perfil and perfil_data:
            for attr, value in perfil_data.items():
                setattr(perfil, attr, value)
            perfil.save()

        return instance
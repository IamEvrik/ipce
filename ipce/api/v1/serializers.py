"""Сериализаторы для API."""

from django.contrib.auth import get_user_model
from rest_framework import serializers

from software import models as softmodels

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователей."""

    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class UserCreateSerializer(serializers.ModelSerializer):
    """Создание пользователя."""

    class Meta:
        model = User
        fields = '__all__'


class OSKeySerializer(serializers.ModelSerializer):
    """Ключи офиса."""

    os = serializers.CharField(source='os_version.name')

    class Meta:
        model = softmodels.OSKey
        fields = ('os', 'key_text', 'note')

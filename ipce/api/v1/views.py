"""Вьюсеты."""

from django.contrib.auth import get_user_model
from rest_framework import viewsets

from api.v1.serializers import OSKeySerializer, UserSerializer
from software import models as softmodels

User = get_user_model()


class UserViewset(viewsets.ModelViewSet):
    """Пользователи."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class OSKeyViewset(viewsets.ModelViewSet):
    """Ключи ОС."""

    queryset = softmodels.OSKey.objects.all()
    serializer_class = OSKeySerializer

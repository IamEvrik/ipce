"""Модели приложения users."""
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Кастомная модель пользователя."""

    class Meta(AbstractUser.Meta):
        pass

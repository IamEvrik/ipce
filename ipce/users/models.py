"""Модели приложения users."""
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Кастомная модель пользователя."""

    class Meta(AbstractUser.Meta):
        verbose_name = _('user')
        verbose_name_plural = _('users')

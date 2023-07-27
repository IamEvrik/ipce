"""Настройки приложения computers."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ComputersConfig(AppConfig):
    """Класс настроек приложения."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'computers'
    verbose_name = _('computers')

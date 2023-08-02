"""Настройки приложения программное обеспечение."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SoftwareConfig(AppConfig):
    """Настройки."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'software'
    verbose_name = _('software')

"""Модели приложения computers."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from computers.validators import validate_office_key


class OfficeVersion(models.Model):
    """Версии офиса."""

    name = models.CharField(_('name'), max_length=100)

    class Meta:
        verbose_name = _('office version')
        verbose_name_plural = _('office versions')


class OfficeKey(models.Model):
    """Ключи для офиса."""

    office_version_id = models.ForeignKey(
        OfficeVersion,
        on_delete=models.CASCADE,
        verbose_name=_('version id'),
        related_name='keys'
    )
    key_text = models.CharField(
        verbose_name=_('key'),
        max_length=40,
        validators=(validate_office_key,)
    )
    note = models.TextField(_('note'))

    class Meta:
        verbose_name = _('office key')
        verbose_name_plural = _('office keys')

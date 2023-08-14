"""Модели приложения software."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from software.validators import validate_key


class AbstractKeyModel(models.Model):
    """Модель ключ и примечание."""

    key_text = models.CharField(
        verbose_name=_('key'),
        max_length=40,
        validators=(validate_key,)
    )
    note = models.TextField(_('note'), blank=True)

    class Meta:
        abstract = True


class OfficeVersion(models.Model):
    """Версии офиса."""

    name = models.CharField(_('name'), max_length=100)

    class Meta:
        verbose_name = _('office version')
        verbose_name_plural = _('office versions')

    def __str__(self) -> str:
        """Строковое представление - название."""
        return f'{self.name}'


class OfficeKey(AbstractKeyModel):
    """Ключи для офиса."""

    office_version = models.ForeignKey(
        OfficeVersion,
        on_delete=models.CASCADE,
        verbose_name=_('office version'),
        related_name='keys'
    )

    class Meta:
        verbose_name = _('office key')
        verbose_name_plural = _('office keys')
        ordering = ('office_version', 'key_text')
        constraints = (
            models.UniqueConstraint(
                fields=('office_version', 'key_text'),
                name='office_key_unique',
            ),
        )

    def __str__(self) -> str:
        """Строковое представление - версия и ключ."""
        return f'{self.office_version} - {self.key_text}'


class OSVersion(models.Model):
    """Версии ОС."""

    name = models.CharField(_('name'), max_length=100)

    class Meta:
        verbose_name = _('OS version')
        verbose_name_plural = _('OS versions')

    def __str__(self) -> str:
        """Название."""
        return f'{self.name}'


class OSKey(AbstractKeyModel):
    """Ключи ОС."""

    os_version = models.ForeignKey(
        OSVersion,
        on_delete=models.CASCADE,
        verbose_name=_('OS version')
    )

    class Meta:
        verbose_name = _('OS key')
        verbose_name_plural = _('OS keys')
        ordering = ('os_version', 'key_text')
        constraints = (
            models.UniqueConstraint(
                fields=('os_version', 'key_text'),
                name='OS_key_unique',
            ),
        )

    def __str__(self) -> str:
        """Версия и ключ."""
        return f'{self.os_version} - {self.key_text}'

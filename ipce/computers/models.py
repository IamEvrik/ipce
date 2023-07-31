"""Модели приложения computers."""

from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _

from computers.validators import (validate_office_key, validate_os_bit_depth,
                                  validate_os_key)


class OfficeVersion(models.Model):
    """Версии офиса."""

    name = models.CharField(_('name'), max_length=100)

    class Meta:
        verbose_name = _('office version')
        verbose_name_plural = _('office versions')

    def __str__(self) -> str:
        """Строковое представление - название."""
        return self.name


class OfficeKey(models.Model):
    """Ключи для офиса."""

    office_version = models.ForeignKey(
        OfficeVersion,
        on_delete=models.CASCADE,
        verbose_name=_('office version'),
        related_name='keys'
    )
    key_text = models.CharField(
        verbose_name=_('key'),
        max_length=40,
        validators=(validate_office_key,)
    )
    note = models.TextField(_('note'), blank=True)

    class Meta:
        verbose_name = _('office key')
        verbose_name_plural = _('office keys')
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
        return self.name


class OSKey(models.Model):
    """Ключи ОС."""

    os_version = models.ForeignKey(
        OSVersion,
        on_delete=models.CASCADE,
        verbose_name=_('OS version')
    )
    key_text = models.CharField(
        verbose_name=_('key'),
        max_length=40,
        validators=(validate_os_key,)
    )
    note = models.TextField(_('note'), blank=True)

    class Meta:
        verbose_name = _('OS key')
        verbose_name_plural = _('OS keys')
        constraints = (
            models.UniqueConstraint(
                fields=('os_version', 'key_text'),
                name='OS_key_unique',
            ),
        )

    def __str__(self) -> str:
        """Версия и ключ."""
        return f'{self.os_version} - {self.key_text}'


class Division(models.Model):
    """Отдел."""

    name = models.CharField(_('name'), max_length=100)

    class Meta:
        verbose_name = _('division')
        verbose_name_plural = _('divisions')

    def __str__(self) -> str:
        """Название."""
        return self.name


class WorkPlace(models.Model):
    """Рабочее место."""

    division = models.ForeignKey(
        Division,
        on_delete=models.SET_NULL,
        verbose_name=_('division'),
        related_name='workplaces',
        blank=True,
        null=True,
    )
    name = models.CharField(_('name'), max_length=100)
    note = models.TextField(_('note'), blank=True)

    class Meta:
        verbose_name = _('work place')
        verbose_name_plural = _('work places')

    def __str__(self) -> str:
        """Строковое представление - название."""
        return self.name


class Computer(models.Model):
    """Компьютер."""

    class OsBitDepth(models.TextChoices):
        """Разрядность ОС."""

        X32 = 'x32'
        X64 = 'x64'
        __empty__ = _('Unknown')

    inventory_number = models.CharField(
        _('inventory number'),
        max_length=10,
        blank=True,
    )
    name = models.CharField(_('name'), max_length=20, blank=True)
    processor = models.CharField(_('processor'), max_length=100, blank=True)
    os_key = models.ForeignKey(
        OSKey,
        on_delete=models.SET_NULL,
        verbose_name=_('OS key'),
        blank=True,
        null=True,
    )
    os_bit_depth = models.CharField(
        verbose_name=_('OS bit depth'),
        max_length=3,
        choices=OsBitDepth.choices,
        blank=True,
    )
    ram_capacity = models.IntegerField(
        verbose_name=_('RAM capacity'),
        validators=(
            validators.MinValueValidator(0, _('negative RAM capacity')),
        )
    )
    has_ssd = models.BooleanField(_('has SSD'), default=False)
    office_key = models.ForeignKey(
        OfficeKey,
        on_delete=models.SET_NULL,
        verbose_name=_('office key'),
        blank=True,
        null=True,
    )
    work_place = models.ForeignKey(
        WorkPlace,
        on_delete=models.SET_NULL,
        verbose_name=_('work place'),
        blank=True,
        null=True,
    )
    user = models.CharField(_('user'), max_length=150, blank=True)
    ip_address = models.GenericIPAddressField(
        verbose_name=_('IP address'),
        protocol='IPv4',
        blank=True,
        null=True,
        unique=True,
    )
    note = models.TextField(_('note'), blank=True)

    class Meta:
        verbose_name = _('computer')
        verbose_name_plural = _('computers')
        default_related_name = 'computer'

    def __str__(self):
        """IP адрес, название, рабочее место."""
        return f'{self.ip_address}, {self.name}, {self.work_place}'


class Monitor(models.Model):
    """Монитор."""

    name = models.CharField(_('monitor'), max_length=255)
    serial_no = models.CharField(_('serial number'), max_length=50)
    work_place = models.ForeignKey(
        WorkPlace,
        verbose_name=_('work place'),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _('monitor')
        verbose_name_plural = _('monitors')
        default_related_name = 'monitor'
        constraints = (
            models.UniqueConstraint(
                fields=('name', 'serial_no'),
                name='unique_monitor_name_serial_no'
            ),
        )

    def __str__(self):
        """Название и серийный номер."""
        return f'{self.name}: {self.serial_no}'

"""Модели приложения computers."""

from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _

from computers.validators import validate_office_key, validate_os_key


class OfficeVersion(models.Model):
    """Версии офиса."""

    name = models.CharField(_('name'), max_length=100)

    class Meta:
        verbose_name = _('office version')
        verbose_name_plural = _('office versions')

    def __str__(self) -> str:
        """Строковое представление - название."""
        return f'{self.name}'


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
        return f'{self.name}'


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
        return f'{self.name}'


class UserName(models.Model):
    """Учетная запись пользователя."""

    name = models.CharField(_('username'), max_length=30, unique=True)
    fio = models.CharField(_('FIO'), max_length=255, blank=True)
    password = models.CharField(_('password'), max_length=100, blank=True)

    class Meta:
        verbose_name = _('username')
        verbose_name_plural = _('usernames')

    def __str__(self):
        """Имя пользователя (ФИО)."""
        return f'{self.name} ({self.fio})'


class Responsible(models.Model):
    """Ответственное лицо."""

    fio = models.CharField(_('FIO'), max_length=255)

    class Meta:
        verbose_name = _('responsible')
        verbose_name_plural = _('responsibles')

    def __str__(self):
        """ФИО."""
        return f'{self.fio}'


class Manufacturer(models.Model):
    """Фирмы-производители."""

    name = models.CharField(_('name'), unique=True, max_length=255)

    class Meta:
        verbose_name = _('manufacturer')
        verbose_name_plural = _('manufacturers')
        ordering = ('name',)

    def __str__(self):
        """Название."""
        return f'{self.name}'


class Accessory(models.Model):
    """Абстрактный класс для комплектующих."""

    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.RESTRICT,
        verbose_name=_('manufacturer'),
    )

    class Meta:
        abstract = True


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
    responsible = models.ForeignKey(
        Responsible,
        verbose_name=_('responsible'),
        on_delete=models.RESTRICT,
    )
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
    has_ssd = models.BooleanField(_('has SSD'), default=False)
    office_key = models.ForeignKey(
        OfficeKey,
        on_delete=models.SET_NULL,
        verbose_name=_('office key'),
        blank=True,
        null=True,
    )
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
        """Название, инвентарный номер, IP-адрес."""
        return f'{self.name}, {self.inventory_number}, {self.ip_address}'


class RAMType(models.Model):
    """Типы ОЗУ."""

    name = models.CharField(_('RAM type'), max_length=10, unique=True)

    class Meta:
        verbose_name = _('RAM type')
        verbose_name_plural = _('RAM types')

    def __str__(self):
        """Название."""
        return f'{self.name}'


class RAM(Accessory):
    """ОЗУ."""

    class RAMCapacity(models.IntegerChoices):
        """Объем ОЗУ."""

        GB1 = 1, '1 GB'
        GB2 = 2, '2 GB'
        GB4 = 4, '4 GB'
        GB8 = 8, '8 GB'
        GB16 = 16, '16 GB'
        GB32 = 32, '32 GB'
        GB64 = 64, '64 GB'
        GB128 = 128, '128 GB'
        GB256 = 256, '256 GB'
        GB512 = 512, '512 GB'
        TB1 = 1024, '1 TB'
        TB2 = 2048, '2 TB'
        TB4 = 4096, '4 TB'
        __empty__ = _('Unknown')

    type = models.ForeignKey(
        RAMType,
        on_delete=models.RESTRICT,
        verbose_name=_('RAM type'),
    )
    capacity = models.IntegerField(
        _('RAM capacity'),
        choices=RAMCapacity.choices,
    )
    serial_no = models.CharField(_('serial number'), max_length=255, blank=True)
    computer = models.ForeignKey(
        to=Computer,
        on_delete=models.RESTRICT,
        verbose_name=_('computer'),
    )

    class Meta:
        verbose_name = _('RAM')
        verbose_name_plural = _('RAM')
        default_related_name = 'ram'

    def __str__(self):
        """Название, тип и объем."""
        return f'{self.manufacturer} {self.capacity} {self.type}'
        

class Monitor(models.Model):
    """Монитор."""

    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete = models.RESTRICT,
        verbose_name=_('manufacturer'),
        related_name='monitor'
    )
    name = models.CharField(_('model'), max_length=255)
    serial_no = models.CharField(_('serial number'), max_length=50)

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


class WorkPlace(models.Model):
    """Рабочее место."""

    division = models.ForeignKey(
        Division,
        on_delete=models.SET_NULL,
        verbose_name=_('division'),
        blank=True,
        null=True,
    )
    name = models.CharField(_('name'), max_length=100)
    username = models.ForeignKey(
        UserName,
        verbose_name=_('username'),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    computer = models.ForeignKey(
        Computer,
        on_delete=models.RESTRICT,
        verbose_name=_('computer'),
    )
    monitor = models.ForeignKey(
        Monitor,
        on_delete=models.RESTRICT,
        verbose_name=_('monitor'),
    )
    note = models.TextField(_('note'), blank=True)

    class Meta:
        verbose_name = _('work place')
        verbose_name_plural = _('work places')
        default_related_name = 'workplace'

    def __str__(self) -> str:
        """Строковое представление - название."""
        return f'{self.name}'


class WorkplaceComputerHistory(models.Model):
    """История рабочих мест и компьютеров."""

    workplace = models.ForeignKey(
        WorkPlace,
        on_delete = models.CASCADE,
        verbose_name=_('work place'),
        related_name='computer_history',
    )
    computer = models.ForeignKey(
        Computer,
        on_delete=models.CASCADE,
        verbose_name=_('computer'),
        related_name='workplace_history',
    )
    install_date = models.DateField(_('install date'))

    class Meta:
        verbose_name = _('Workplace computers')
        verbose_name_plural = _('workplaces computers')
        constraints = (
            models.UniqueConstraint(
                fields=('workplace', 'computer', 'install_date'),
                name='unique_workplace_computer_history'
            ),
        )
        

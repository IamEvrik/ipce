"""Модели приложения computers."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from software import models as softmodels


class AbstractSerialNoModel(models.Model):
    """Базовая модель с серийным номером."""

    serial_no = models.CharField(
        _('serial number'),
        max_length=255,
    )

    class Meta:
        abstract = True


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


class AbstractManufacturerModel(models.Model):
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
        softmodels.OSKey,
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
    office_key = models.ForeignKey(
        softmodels.OfficeKey,
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


class MemoryCapacity(models.Model):
    """Объемы памяти."""

    capacity = models.CharField(_('capacity'), max_length=10, unique=True)

    class Meta:
        verbose_name = _('memory capacity')
        verbose_name_plural = _('memory capacities')
        ordering = ('capacity',)

    def __str__(self):
        """Объем."""
        return f'{self.capacity}'


class RAMModel(AbstractManufacturerModel):
    """Модели ОЗУ."""

    ram_type = models.ForeignKey(
        RAMType,
        on_delete=models.RESTRICT,
        verbose_name=_('RAM type'),
    )
    capacity = models.ForeignKey(
        to=MemoryCapacity,
        on_delete=models.RESTRICT,
        verbose_name=_('memory capacity'),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _('RAM model')
        verbose_name_plural = _('RAM models')
        default_related_name = 'ram_model'

    def __str__(self):
        """Производитель объем тип."""
        return f'{self.manufacturer} {self.capacity} {self.ram_type}'


class RAM(AbstractSerialNoModel):
    """ОЗУ."""

    ram_model = models.ForeignKey(
        RAMModel,
        on_delete=models.RESTRICT,
        verbose_name=_('RAM model'),
    )
    computer = models.ForeignKey(
        to=Computer,
        on_delete=models.RESTRICT,
        verbose_name=_('computer'),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('RAM')
        verbose_name_plural = _('RAM')
        default_related_name = 'ram'

    def __str__(self):
        """Модель серийный номер."""
        return f'{self.ram_model} {self.serial_no}'


class Monitor(AbstractManufacturerModel, AbstractSerialNoModel):
    """Монитор."""

    name = models.CharField(_('model'), max_length=255)

    class Meta:
        verbose_name = _('monitor')
        verbose_name_plural = _('monitors')
        default_related_name = 'monitor'

    def __str__(self):
        """Название и серийный номер."""
        return f'{self.name}: {self.serial_no}'


class HDDType(models.Model):
    """Тип жесткого диска."""

    name = models.CharField(_('name'), max_length=10, unique=True)

    class Meta:
        verbose_name = _('hdd type')
        verbose_name_plural = _('hdd types')

    def __str__(self):
        """Название."""
        return f'{self.name}'


class HDD(AbstractManufacturerModel, AbstractSerialNoModel):
    """Жесткий диск."""

    model = models.CharField(_('model'), max_length=100)
    hdd_type = models.ForeignKey(
        to=HDDType,
        on_delete=models.RESTRICT,
        verbose_name=_('hdd type'),
        blank=True,
        null=True,
    )
    capacity = models.ForeignKey(
        to=MemoryCapacity,
        on_delete=models.RESTRICT,
    )
    computer = models.ForeignKey(
        to=Computer,
        on_delete=models.RESTRICT,
        verbose_name=_('computer'),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('HDD')
        verbose_name_plural = _('HDDs')
        default_related_name = 'hdd'

    def __str__(self):
        """Тип, производитель, объем."""
        return f'{self.hdd_type} {self.manufacturer} {self.capacity}'


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
        on_delete=models.CASCADE,
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

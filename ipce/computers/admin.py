"""Настройки админки для приложения computers."""

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from computers import models as mymodels
from software import models as softmodels
from users import models as usermodels


class IPCEAdminSite(admin.AdminSite):
    """Настройка админки."""

    site_header = _('YPS admin')
    site_title = _('YPS admin portal')
    index_title = _('Administration')


ipce_admin = IPCEAdminSite(name='ipce_admin')


@admin.register(mymodels.WorkPlace, site=ipce_admin)
class AdminWorkPlace(admin.ModelAdmin):
    """Отображение рабочего места."""

    list_display = (
        'name',
        'computer',
        'get_ip_address',
        'username',
        'monitor'
    )
    readonly_fields = ('get_ip_address',)
    empty_value_display = _('Unknown')

    @admin.display(
        ordering='computer__ip_address',
        description=_('IP address'),
    )
    def get_ip_address(self, obj):
        """Отдельное отображение IP адреса."""
        return obj.computer.ip_address


@admin.register(mymodels.Monitor, site=ipce_admin)
class AdminMonitor(admin.ModelAdmin):
    """Отображение мониторов в админке."""

    fields = ('manufacturer', 'name', 'serial_no')


@admin.register(mymodels.RAMModel, site=ipce_admin)
class AdminRAM(admin.ModelAdmin):
    """Отображение ОЗУ в админке."""

    fields = ('manufacturer', 'ram_type', 'capacity')


@admin.register(mymodels.HDDModel, site=ipce_admin)
class AdminHDDModel(admin.ModelAdmin):
    """Отображение моделей жестких дисков."""

    fields = ('manufacturer', 'hdd_type', 'model', 'capacity')


ipce_admin.register(mymodels.Manufacturer)
ipce_admin.register(mymodels.MemoryCapacity)
ipce_admin.register(mymodels.RAMType)
ipce_admin.register(mymodels.RAM)
ipce_admin.register(mymodels.Division)
ipce_admin.register(mymodels.UserName)
ipce_admin.register(mymodels.Responsible)
ipce_admin.register(mymodels.WorkplaceComputerHistory)
ipce_admin.register(mymodels.HDDType)
ipce_admin.register(mymodels.HDD)
ipce_admin.register(mymodels.Computer)


@admin.register(softmodels.OfficeKey, site=ipce_admin)
class AdminOfficeKey(admin.ModelAdmin):
    """Отображение ключей офиса в админке."""

    fields = ('office_version', 'key_text', 'note')


@admin.register(softmodels.OSKey, site=ipce_admin)
class AdminOSKey(admin.ModelAdmin):
    """Отображение ключей офиса в админке."""

    fields = ('os_version', 'key_text', 'note')


ipce_admin.register(softmodels.OfficeVersion)
ipce_admin.register(softmodels.OSVersion)


ipce_admin.register(usermodels.User)

"""Настройки админки для приложения computers."""

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from computers import models as mymodels
from users import models as usermodels


@admin.register(mymodels.WorkPlace)
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
        description=_('IP address')
    )
    def get_ip_address(self, obj):
        """Отдельное отображение IP адреса."""
        return obj.computer.ip_address


class InlineComputerRAM(admin.TabularInline):
    """Отображение памяти в компьютере."""

    model = mymodels.RAM
    extra = 1


@admin.register(mymodels.Computer)
class AdminComputer(admin.ModelAdmin):
    """Отображение компьютеров в админке."""

    inlines = [
        InlineComputerRAM
    ]


admin.site.register(mymodels.OfficeKey)
admin.site.register(mymodels.OfficeVersion)
admin.site.register(mymodels.OSKey)
admin.site.register(mymodels.OSVersion)
admin.site.register(mymodels.Manufacturer)
admin.site.register(mymodels.MemoryCapacity)
admin.site.register(mymodels.RAMType)
admin.site.register(mymodels.RAM)
admin.site.register(mymodels.Division)
admin.site.register(mymodels.Monitor)
admin.site.register(mymodels.UserName)
admin.site.register(mymodels.Responsible)
admin.site.register(mymodels.WorkplaceComputerHistory)

admin.site.register(usermodels.User)

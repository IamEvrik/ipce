"""Настройки админки для приложения computers."""

from django.contrib import admin

from computers.models import OfficeKey, OfficeVersion

admin.site.register(OfficeKey)
admin.site.register(OfficeVersion)

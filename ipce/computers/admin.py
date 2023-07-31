"""Настройки админки для приложения computers."""

from django.contrib import admin

from computers import models as mymodels
from users import models as usermodels

admin.site.register(mymodels.OfficeKey)
admin.site.register(mymodels.OfficeVersion)
admin.site.register(mymodels.OSKey)
admin.site.register(mymodels.OSVersion)
admin.site.register(mymodels.Computer)
admin.site.register(mymodels.Division)
admin.site.register(mymodels.WorkPlace)
admin.site.register(mymodels.Monitor)
admin.site.register(mymodels.UserName)

admin.site.register(usermodels.User)

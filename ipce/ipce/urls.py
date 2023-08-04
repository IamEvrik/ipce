"""URL configuration for ipce project."""

from django.urls import path

from computers.admin import ipce_admin

urlpatterns = [
    path('admin/', ipce_admin.urls),
]

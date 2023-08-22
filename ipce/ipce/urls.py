"""URL configuration for ipce project."""

from django.urls import include, path

from computers.admin import ipce_admin

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', ipce_admin.urls),
]

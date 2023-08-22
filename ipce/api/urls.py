"""URL для API."""

from django.urls import include, path
from rest_framework import routers

from api.v1 import views as v1views

v1_router = routers.DefaultRouter()
v1_router.register('users', v1views.UserViewset)
v1_router.register('oskeys', v1views.OSKeyViewset)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='drfm')),
]

from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from androidapi.api import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register('usuarios', views.UsuarioViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.Index.as_view(), name="Index"),
    url('api/', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
]
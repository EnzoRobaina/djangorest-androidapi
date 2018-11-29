from django.conf.urls import url, include
from rest_framework import routers
from androidapi.api import views

router = routers.DefaultRouter()
router.register('usuarios', views.UsuarioViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('', include(router.urls)),
    url('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
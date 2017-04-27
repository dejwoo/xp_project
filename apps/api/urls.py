from django.conf.urls import *
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = DefaultRouter()

router.register(r'users', views.UserViewSet, 'user')
router.register(r'gateways', views.GatewayListViewSet, 'gateway')
router.register(r'nodes', views.NodeListViewSet, 'node')
router.register(r'swarms', views.SwarmListViewSet, 'swarm')
urlpatterns = [
    url(r'^', include(router.urls))
]

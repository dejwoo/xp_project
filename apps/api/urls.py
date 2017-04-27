from django.conf.urls import *
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, 'list')
router.register(r'gateways', views.GatewayListViewSet, 'gateways')
router.register(r'nodes', views.NodeListViewSet, 'nodes')
router.register(r'swarms', views.SwarmListViewSet, 'swarms')
urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^gateways/(?P<pk>[0-9]+)$', views.GatewayDetailView.as_view(), name='gateway'),
    url(r'^gateways/(?P<pk>[0-9]+)/data$', views.GatewayDetailView.as_view(), name='gatewayData'),

    url(r'^node$', views.NodeDetailView.as_view(), name='node'),
    url(r'^node/(?P<pk>[0-9]+)/data$', views.NodeDetailView.as_view(), name='nodeData'),

    url(r'^swarm$', views.SwarmDetailView.as_view(), name='swarm'),
    url(r'^swarm/(?P<pk>[0-9]+)/data$', views.SwarmDetailView.as_view(), name='swarmData'),

]

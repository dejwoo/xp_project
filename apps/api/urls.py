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

    #url(r'^user/(?P<pk>[0-9]+)$', views.UserView.as_view(), names='user'),
    #url(r'^user/(?P<pk>[0-9]+)/data$', views.UserDataView.as_view(), names='userData'),

    #url(r'^node$', views.NodeView.as_view(), name='node'),
    #url(r'^node/(?P<pk>[0-9]+)/data$', views.NodeDataView.as_view(), name='nodeData'),

    #url(r'^swarm$', views.SwarmView.as_view(), name='swarm'),
    #url(r'^swarm/(?P<pk>[0-9]+)/data$', views.SwarmDataView.as_view(), name='swarmData'),

]

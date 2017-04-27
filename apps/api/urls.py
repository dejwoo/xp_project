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
    url(r'^', include(router.urls)),
    url(r'^$', views.api_root),

    #url(r'^gateway/(?P<pk>[0-9]+)$', views.GatewayDetailView.as_view(), name='gateway'),
    #url(r'^gateway/(?P<pk>[0-9]+)/data$', views.GatewayDetailView.as_view(), name='gateway-detail'),

    #url(r'^node$', views.NodeDetailView.as_view(), name='node'),
    #url(r'^node/(?P<pk>[0-9]+)/data$', views.NodeDetailView.as_view(), name='node-detail'),

    #url(r'^swarm$', views.SwarmDetailView.as_view(), name='swarm'),
    #url(r'^swarm/(?P<pk>[0-9]+)/data$', views.SwarmDetailView.as_view(), name='swarm-detail'),

]

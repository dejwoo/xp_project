from django.http import Http404
from rest_framework.decorators import detail_route
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import viewsets, status, mixins, generics, permissions
from rest_framework.views import APIView
from apps.api.permissions import IsStaffOrTargetUser
from apps.api.models import *
from apps.api.serializers import UserSerializer, GatewaySerializer, NodeSerializer, SwarmSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @detail_route(methods=['get'])
    def data(self, request, pk=None):
        user = self.get_object()

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny(),)


class GatewayListViewSet(viewsets.ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
    permission_classes = (permissions.AllowAny,)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class GatewayDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
    permission_classes = (permissions.AllowAny,)


class NodeListViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = (permissions.AllowAny,)


class NodeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = (permissions.AllowAny,)


class SwarmListViewSet(viewsets.ModelViewSet):
    queryset = Swarm.objects.all()
    serializer_class = SwarmSerializer
    permission_classes = (permissions.AllowAny,)


class SwarmDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Swarm.objects.all()
    serializer_class = SwarmSerializer
    permission_classes = (permissions.AllowAny,)

from django.http import Http404
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import detail_route, api_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import viewsets, status, mixins, generics, permissions
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from apps.api.permissions import IsStaffOrTargetUser, IsOwnerOrReadOnly
from apps.api.models import *
from apps.api.serializers import UserSerializer, GatewaySerializer, NodeSerializer, SwarmSerializer
from rest_framework_jwt.views import obtain_jwt_token


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny, permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(methods=['get'])
    def data(self, request, pk=None):
        user = self.get_object()


class GatewayListViewSet(viewsets.ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
    permission_classes = (AllowAny, permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    #def list(self, request, *args, **kwargs):
    #    return super().list(request, *args, **kwargs)


class GatewayDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
    permission_classes = (AllowAny, permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class NodeListViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = (AllowAny, permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class NodeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = (AllowAny, permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class SwarmListViewSet(viewsets.ModelViewSet):
    queryset = Swarm.objects.all()
    serializer_class = SwarmSerializer
    permission_classes = (AllowAny, permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class SwarmDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Swarm.objects.all()
    serializer_class = SwarmSerializer
    permission_classes = (AllowAny, permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

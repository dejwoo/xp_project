from rest_framework.decorators import list_route, detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from apps.api.models import *
from apps.api.serializers import UserSerializer, GatewaySerializer, NodeSerializer, SwarmSerializer, MessageSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        else:
            return User.objects.filter(id=self.request.user.id)


class GatewayListViewSet(viewsets.ModelViewSet):
    serializer_class = GatewaySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Gateway.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = GatewaySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['get'])
    def data(self, request, pk=None):
        try:
            messages_trough_gateway = Message.objects.filter(rxInfo__gateway__mac=Gateway.objects.get(id=pk).mac)
        except Exception as e:
            return Response("Gateway not found", status=status.HTTP_404_NOT_FOUND)
        page = self.paginate_queryset(messages_trough_gateway)
        if page is not None:
            serializer = MessageSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = MessageSerializer(messages_trough_gateway, many=True)
        return Response(serializer.data)


class NodeListViewSet(viewsets.ModelViewSet):
    serializer_class = NodeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Node.objects.all()
        else:
            return Node.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = NodeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['get'])
    def data(self, request, pk=None):
        try:
            messages_trough_node = Message.objects.filter(devEUI=Node.objects.get(id=pk).dev_eui)
        except Exception as e:
            return Response("Node not found", status=status.HTTP_404_NOT_FOUND)
        page = self.paginate_queryset(messages_trough_node)
        if page is not None:
            serializer = MessageSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = MessageSerializer(messages_trough_node, many=True)
        return Response(serializer.data)


class SwarmListViewSet(viewsets.ModelViewSet):
    serializer_class = SwarmSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Swarm.objects.all()
        else:
            return Swarm.objects.filter(user_id=self.request.user.id)

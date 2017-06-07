from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response

from apps.api.permissions import IsStaffOrTargetUser, IsOwnerOrReadOnly
from apps.api.models import *
from apps.api.serializers import UserSerializer, GatewaySerializer, NodeSerializer, SwarmSerializer
from django.http import HttpResponseBadRequest

class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)# + (IsStaffOrTargetUser, )

    def get_queryset(self):
        """
        Filter objects so a user only sees his own stuff.
        If user is admin, let him see all.
        """
        if self.request.user.is_staff:
            return User.objects.all()
        else:
            return User.objects.filter(id=self.request.user.id)


class GatewayListViewSet(viewsets.ModelViewSet):
    serializer_class = GatewaySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print(Gateway.objects.all())
        if self.request.user.is_staff:
            return Gateway.objects.all()
        else:
            return Gateway.objects.filter(user__id=self.request.user.id)


class NodeListViewSet(viewsets.ModelViewSet):
    serializer_class = NodeSerializer
    permission_classes = (IsAuthenticated, )

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

class SwarmListViewSet(viewsets.ModelViewSet):
    serializer_class = SwarmSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Swarm.objects.all()
        else:
            return Swarm.objects.filter(user_id=self.request.user.id)

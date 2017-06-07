from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, generics, permissions
from apps.api.permissions import IsStaffOrTargetUser, IsOwnerOrReadOnly
from apps.api.models import *
from apps.api.serializers import UserSerializer, GatewaySerializer, NodeSerializer, SwarmSerializer


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
        if self.request.user.is_staff or self.request.user.gateways == None:
            return Gateway.objects.all()
        else:
            return self.request.user.gateways.all()


class GatewayDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
    permission_classes = (IsStaffOrTargetUser, IsAuthenticated)


class NodeListViewSet(viewsets.ModelViewSet):
    serializer_class = NodeSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.nodes == None:
            return Node.objects.all()
        else:
            return self.request.user.nodes.all()


class NodeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = (IsStaffOrTargetUser, IsAuthenticated)


class SwarmListViewSet(viewsets.ModelViewSet):
    serializer_class = SwarmSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.gateways == None:
            return Swarm.objects.all()
        else:
            return self.request.user.nodes.all()


class SwarmDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Swarm.objects.all()
    serializer_class = SwarmSerializer
    permission_classes = (AllowAny, permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

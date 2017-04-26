from rest_framework.decorators import detail_route
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import viewsets
from apps.api.permissions import IsStaffOrTargetUser
from apps.api.models import *


class IndexView(CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "api/index.html"

    def get(self, request, *args, **kwargs):
        context = {'some_dynamic_value': 'This text comes from django view!', }
        return Response(context)

    def post(self, request, *args, **kwargs):
        pass


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @detail_route(methods=['get'])
    def data(self, request, pk=None):
        user = self.get_object()

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST' else IsStaffOrTargetUser()),


class GatewayListViewSet(viewsets.ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer


class NodeListViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class SwarmListViewSet(viewsets.ModelViewSet):
    queryset = Swarm.objects.all()
    serializer_class = SwarmSerializer

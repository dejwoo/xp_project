from rest_framework import mixins
from rest_framework.generics import CreateAPIView, ListCreateAPIView, GenericAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class IndexView(CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "api/index.html"

    def get(self, request, *args, **kwargs):
        context = {
            'some_dynamic_value': 'This text comes from django view!',
        }
        return Response(context)

    def post(self, request, *args, **kwargs):
        pass


class UserListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.DestroyModelMixin, mixins.UpdateModelMixin,
                      GenericAPIView):
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class UserView(GenericAPIView):
    pass


class UserDataView(GenericAPIView):
    pass


class GatewayListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                         mixins.DestroyModelMixin, mixins.UpdateModelMixin,
                         GenericAPIView):
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class NodeListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.DestroyModelMixin, mixins.UpdateModelMixin,
                      GenericAPIView):
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class SwarmListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                       mixins.DestroyModelMixin, mixins.UpdateModelMixin,
                       GenericAPIView):
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

from django.conf.urls import *
from rest_framework.routers import DefaultRouter

from apps.api.views import UserListViewSet
from . import views

router = DefaultRouter()
router.register(r'users', UserListViewSet)
urlpatterns = router.urls
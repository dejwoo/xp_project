from django.conf.urls import *
from django.contrib import admin

from apps.api import urls as api_urls
from apps.web import urls as web_urls
from material.frontend import urls as frontend_urls

urlpatterns = (
    url(r'', include(web_urls)),
    url(r'api/', include(api_urls)),
    url(r'^admin/', include(admin.site.urls)),
)

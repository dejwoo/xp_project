from django.conf.urls import *
from django.contrib import admin
from apps.api import urls as api_urls
from apps.web import urls as web_urls

urlpatterns = (
    url(r'api/', include(api_urls)),
    url(r'web/', include(web_urls)),
    url(r'^admin/', admin.site.urls),
)

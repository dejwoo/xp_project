from django.conf.urls import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'web/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'web/logged_out.html'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^accounts/profile/', views.logged_in, {'template_name': 'web/dashboard.html'}, name='dashboard'),
)

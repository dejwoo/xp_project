from django.conf.urls import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'web/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'web/logged_out.html'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^accounts/dashboard/', views.DashboardView.as_view(), name='dashboard'),
    url(r'^create-api-token',views.createBasicApiToken, name='create-basic-token')
    #TODO implement profile page
    #url(r'^accounts/profile/(?P<pk>[0-9]+)', views.ProfilePageView.as_view(), name='profile_page'),
)

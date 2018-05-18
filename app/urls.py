# -*- coding: utf-8 -*-
from django.conf.urls import include
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^en/$', views.index, name='index'),
    url(r'^lang/(?P<lang>\w+)/$', views.set_language, name='set_language'),
    url(r'^checks/new/$', views.checks_new, name='checks_new'),
    url(r'^checks/create/$', views.checks_create, name='checks_create'),
    url(r'^checks/finalize/(?P<pk>\d+)/$', views.checks_finalize, name='checks_finalize'),
    url(r'^checks/show/(?P<pk>\d+)/$', views.checks_show, name='checks_show'),
    url(r'^checks/index/$', views.checks_index, name='checks_index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^services/index/$', views.services_index, name='services_index'),
    url(r'^$', views.index, name='index'),
]

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
    url(r'^$', views.index, name='index'),
]

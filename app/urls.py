# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('en/', views.index, name='index'),
    path('lang/<str:lang>/', views.set_language, name='set_language'),
    path('checks/new/', views.checks_new, name='checks_new'),
    path('checks/create/', views.checks_create, name='checks_create'),
    path('checks/finalize/<int:pk>/', views.checks_finalize, name='checks_finalize'),
    path('checks/show/<int:pk>/', views.checks_show, name='checks_show'),
    path('checks/index/', views.checks_index, name='checks_index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('services/index/', views.services_index, name='services_index'),
    path('favicon\.ico',RedirectView.as_view(url='/static/images/favicon.ico')),
    path('', views.index, name='index'),
]

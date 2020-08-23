from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('noPage/', views.noPage, name='noPage'),
    path('success/', views.successView, name='success'),
]
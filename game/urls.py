from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('getform/', views.getform),
    path('clgame/', views.GuessGameViev.as_view())
]
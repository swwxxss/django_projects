from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('hello/<str:name>', views.hello),
    path('hello2' , views.hello2),
    path('calc/<int:a>/<int:b>', views.calc),

]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('a', views.about),
    path('s', views.service),
    path('f', views.feedback),
    path('c', views.contact),

]
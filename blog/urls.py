from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('about/', views.about_us, name='about'),
    path('contact/', views.contact_us(), name='contact'),
]
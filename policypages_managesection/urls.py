from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('managesection',views.manage_section, name="managesection"),
    path('policypages', views.policy_pages, name="policypages"),
]

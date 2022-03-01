from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('',views.user_auth, name='user_auth'),
]

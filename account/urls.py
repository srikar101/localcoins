from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('', views.logout_view, name="logout"),
    path('activate-user/<uid>/<token>', views.activate_user, name="activate"),  
]

from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('userbuyrequest/<user>',views.user_buy_request, name="userbuyrequest"),
    path('sendtraderequest/<int:id>', views.send_traderequest, name="sendtraderequest"),
    path('traderequest', views.get_traderequest, name="traderequest"),
]

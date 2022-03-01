import imp
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('paymentwindows', views.payment_window, name='paymentwindows'),
    path('paymentwindows/editwindow/<int:id>',views.edit_window, name="editwindow"),
    path('paymentwindows/deletewindow/<int:id>',views.delete_window, name="deletewindow"),
]

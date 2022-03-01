import imp
from django.urls import path
from . import views

urlpatterns = [
    path('fiatgateways', views.fiat_gateways, name="fiatgateways"),
    path('addgateways', views.add_gateways, name="addgateways"),
    path('fiatgateways/edit/<int:id>', views.edit_gateway, name="editgateway"),
]

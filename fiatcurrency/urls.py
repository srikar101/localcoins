from unicodedata import name
from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('fiatcurrencies', views.fiat_currencies, name="fiatcurrencies"),
    path('addfiatcurrencies', views.add_fiatcurrencies, name="addfiatcurrencies"),
    path('fiatcurrencies/edit/<int:id>', views.edit_fiatcurrency, name="editfiatcurrency"),
]

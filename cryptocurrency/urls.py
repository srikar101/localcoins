from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('home/findoffers', views.find_offers, name="findoffers"),
    path('home/buy', views.buy_to_allusers, name='buytoallusers'),
    path('buy', views.buy_crypto, name='buycrypto'),
    path('sell', views.sell_crypto, name='sellcrypto'),
    path('home/sell', views.sell_to_allusers, name='selltoallusers'),
]

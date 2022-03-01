from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('new_advertisement', views.new_advertisement, name='newadd'),
    path('post_advertisement', views.post_advertisement, name="postadd"),
    path('get_myadvertisement', views.get_advertisements, name="getmyadd"),
    path('latest_advertisement', views.latest_advertisement, name="latestadd"),
]

from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('',views.admin_page, name='adminpage'),
    path('cryptocurrency', views.crypto_currency, name="cryptocurrency"),
    path('cryptocurrency/edit/<int:id>', views.edit_crypto, name="editcrypto"),
    path('addcryptocurrency', views.add_crypto, name="addcrypto"),
    path('admintraderequest', views.trade_request, name="admintraderequest"),
    path('all_users', views.all_users, name="allusers"),
    path('all_users/deleteuser/<int:id>', views.delete_user, name="deleteuser"),
    path('all_users/edituser/<int:id>', views.edit_user, name="edituser"),
    path('advertisements', views.all_advertisement, name="alladvertisements"),
    path('transactionlogs', views.all_transaction, name="alltransactions"),
    path('admindashboard', views.dashboard, name="admindashboard"),
]

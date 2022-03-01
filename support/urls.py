from django.urls import path
from . import views

urlpatterns = [
    path('supportticket', views.post_support_tickets, name="supportticket"),
    path('mysupportticket', views.get_my_support_tickets, name='mysupportticket'),
]

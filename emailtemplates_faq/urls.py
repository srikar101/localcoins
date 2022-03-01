from django.urls import path

from . import views

urlpatterns = [
    path('emailtemplates', views.email_templates , name="emailtemplates"),
    path('faq', views.get_FAQ, name="faq"),
    path('faq/edit/<int:id>', views.edit_faq, name="editfaq"),
    path('faq/delete/<int:id>', views.delete_faq, name="deletefaq"),
    path('addfaq', views.add_faq, name="addfaq"),
]

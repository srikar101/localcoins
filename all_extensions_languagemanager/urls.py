from django.urls import path
from . import views

urlpatterns = [
    path('getextensions', views.get_extensions, name="extensions"),
    path('languagemanager', views.all_languages, name='languagemanager'),
    path('addlanguage', views.add_language, name="addlanguage"),
    path('languagemanager/edit/<int:id>', views.edit_language, name='editlanguage'),
    path('languagemanager/delete/<int:id>', views.delete_language, name="deletelanguage"),
]

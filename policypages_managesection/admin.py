from django.contrib import admin

from policypages_managesection.models import ManageSection, PolicyPages

# Register your models here.
admin.site.register(PolicyPages)
admin.site.register(ManageSection)

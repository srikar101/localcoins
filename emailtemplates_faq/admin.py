from django.contrib import admin

from emailtemplates_faq.models import FAQ, EmailTemplates

# Register your models here.

admin.site.register(EmailTemplates)
admin.site.register(FAQ)

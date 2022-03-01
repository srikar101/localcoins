from django.db import models

# Create your models here.

class Extension(models.Model):
    image = models.ImageField(upload_to='logo_extension')
    extension_name = models.CharField(max_length=30)

    def __str__(self):
        return self.extension_name

class LanguageManager(models.Model):
    language_name = models.CharField(max_length=30)
    code = models.CharField(max_length=20)
    default = models.BooleanField(default=False)
from datetime import datetime
from django.db import models

# Create your models here.

class Register(models.Model):
    username = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=100)
    mobile_number = models.IntegerField(null=True)
    country = models.CharField(max_length=30, default='')
    password = models.CharField(max_length=50)
    is_email_verified = models.BooleanField(default=False)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
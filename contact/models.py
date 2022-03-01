from email import message
from urllib import request
from django.db import models

# Create your models here.

class Contact(models.Model):
    username = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50, default='')
    message = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

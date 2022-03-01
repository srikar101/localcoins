from datetime import datetime
import email
from email import message
from django.db import models

# Create your models here.

class Support(models.Model):
    support_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    priority = models.CharField(max_length=30)
    message = models.TextField()
    attachments = models.ImageField(upload_to="pics")
    created_datetime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.support_name


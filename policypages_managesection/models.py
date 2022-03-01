from django.db import models

# Create your models her

class PolicyPages(models.Model):
    title = models.CharField(max_length=30)


    def __str__(self):
        return self.title


class ManageSection(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)

    def __str__(self):
        return self.name
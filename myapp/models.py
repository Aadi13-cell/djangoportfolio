from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=100)

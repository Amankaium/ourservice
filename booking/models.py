from django.db import models

# Create your models here.
class Apartment(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    coutry = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    description = models.TextField()
    

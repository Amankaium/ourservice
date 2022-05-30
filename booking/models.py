from django.db import models

# Create your models here.
class Apartment(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255, default='')
    guest = models.PositiveIntegerField(default=0)
    bed = models.PositiveIntegerField(default=0)
    room = models.PositiveIntegerField(default=0)
    bath = models.PositiveIntegerField(default=0)
    building = models.PositiveIntegerField(default=0)
    flat = models.PositiveIntegerField(default=0, null=True, blank=True)
    wifi = models.CharField(max_length=255, default='')
    tv = models.CharField(max_length=255, default='')
    kitchen = models.CharField(max_length=255, default='')
    washmash = models.CharField(max_length=255, default='')
    conditioner = models.CharField(max_length=255, default='')
    medicine = models.CharField(max_length=255, default='')
    # photo = models.CharField(max_length=255, default='')    

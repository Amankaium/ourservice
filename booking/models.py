from django.db import models

# Create your models here.
class Apartment(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    country = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    type = models.CharField(max_length=255, default='', null=True, blank=True)
    guest = models.PositiveIntegerField(default=0)
    bed = models.PositiveIntegerField(default=0)
    room = models.PositiveIntegerField(default=0)
    bath = models.PositiveIntegerField(default=0)
    building = models.PositiveIntegerField(default=0, null=True, blank=True)
    flat = models.PositiveIntegerField(default=0, null=True, blank=True)
    wifi = models.CharField(max_length=255, default='', null=True, blank=True)
    tv = models.CharField(max_length=255, default='', null=True, blank=True)
    kitchen = models.CharField(max_length=255, default='', null=True, blank=True)
    washmash = models.CharField(max_length=255, default='', null=True, blank=True)
    conditioner = models.CharField(max_length=255, default='', null=True, blank=True)
    medicine = models.CharField(max_length=255, default='', null=True, blank=True)
    photo = models.ImageField(upload_to="apartments/", null=True)    

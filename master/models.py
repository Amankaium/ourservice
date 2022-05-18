from django.db import models

# Create your models here.
class Master(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)  
    photo = models.ImageField(null=True, blank=True)

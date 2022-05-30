from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artist(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    name = models.CharField(max_length=255, null=True)
    genre = models.CharField(max_length=255, null=True)


class Art(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    description = models.TextField(null=True, blank=True)
    artist = models.ForeignKey(to=Artist, on_delete=models.CASCADE)
    genre = models.CharField(max_length=255)
    year = models.IntegerField()
    material = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    dimension = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="arts/", null=True)


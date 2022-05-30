from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Flight(models.Model):
    from_city = models.CharField(max_length=255)
    to_city = models.CharField(max_length=255)
    duration = models.IntegerField(verbose_name="Flight duration in minutes")
    start = models.DateTimeField()
    end = models.DateTimeField()
    aviacompany = models.CharField(max_length=255, null=True)
    price = models.PositiveIntegerField(default=0)


class Passenger(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    document = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True, blank=True)
    date_birth = models.CharField(max_length=255)
    document_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True, blank=True)

    
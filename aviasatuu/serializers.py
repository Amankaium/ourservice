from rest_framework import serializers
from .models import Flight, Passenger


class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flight
        fields = [field.name for field in Flight._meta.get_fields()]


class PassengerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Passenger
        fields = [field.name for field in model._meta.get_fields()]

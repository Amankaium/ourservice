from django.shortcuts import render
from .models import Passenger, Flight
from .serializers import PassengerSerializer, FlightSerializer
from rest_framework import viewsets

# Create your views here.
class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


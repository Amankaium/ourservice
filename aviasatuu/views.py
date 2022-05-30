from django.shortcuts import render
from .models import Passenger, Flight
from .serializers import PassengerSerializer, FlightSerializer
from rest_framework import viewsets
from .filters import FlightFilter

# Create your views here.
class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    filterset_fields = ["name", "surname", "gender", "document"]
    search_fields = ["name", "surname", "gender", "phone", "document_number", "email"]


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filterset_class = FlightFilter
    search_fields = ["from_city", "to_city", "aviacompany"]



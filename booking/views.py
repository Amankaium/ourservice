from django.shortcuts import render
from .models import Apartment
from rest_framework import viewsets
from .serializers import ApartmentSerializer
from .filters import ApartmentsFilter


# Create your views here.
class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filterset_class = ApartmentsFilter
    search_fields = ["title", "country", "description", "city"]


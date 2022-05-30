from django.shortcuts import render
from rest_framework import viewsets
from .models import Art, Artist
from .seriazliers import *

# Create your views here.
class ArtViewSet(viewsets.ModelViewSet):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

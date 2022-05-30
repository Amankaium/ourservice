from django.shortcuts import render
from rest_framework import viewsets 
from .models import Art, Artist
from .seriazliers import *
from .filters import ArtFilter

# Create your views here.
class ArtViewSet(viewsets.ModelViewSet):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer
    filterset_class = ArtFilter
    search_fields = ["name", "genre", "material", "status", "description"]

    def perform_create(self, serializer):
        serializer.validated_data["artist_id"] = 1
        return super().perform_create(serializer)
    

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filterset_fields = ["user__username", "user__first_name", "name", "genre"]
    search_fields = ["user__username", "user__first_name", "name", "genre", "description"]

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MasterSerializer
from .models import Master


class MasterViewSet(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

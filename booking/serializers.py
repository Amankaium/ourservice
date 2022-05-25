from .models import Apartment
from rest_framework import serializers


class ApartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apartment
        fields = "__all__"
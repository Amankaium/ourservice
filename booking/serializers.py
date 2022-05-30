from .models import Apartment
from rest_framework import serializers


class ApartmentSerializer(serializers.HyperlinkedModelSerializer):
    photo = serializers.ImageField(required=True)

    class Meta:
        model = Apartment
        fields = [field.name for field in Apartment._meta.get_fields()]

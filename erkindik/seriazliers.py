from rest_framework import serializers
from .models import *
from users.serializers import UserSerializer


class ArtistSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Artist
        fields = '__all__'


class ArtSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(required=False)

    class Meta:
        model = Art
        fields = [field.name for field in Art._meta.get_fields()]


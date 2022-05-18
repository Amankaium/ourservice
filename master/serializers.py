from rest_framework import serializers
from .models import Master

class MasterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Master
        fields = ['id', 'name', 'description', "price", "photo"]

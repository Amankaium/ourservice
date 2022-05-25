from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.serializers import Serializer, ModelSerializer, CharField


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class IssueTokenRequestSerializer(Serializer):
    model = User

    username = CharField(required=True)
    password = CharField(required=True)


class TokenSeriazliser(ModelSerializer):

    class Meta:
        model = Token
        fields = ['key']
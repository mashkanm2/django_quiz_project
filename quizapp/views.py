
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import serializers

from .models import AuthUser

class UserSerializer(serializers.ModelSerializer):
    class Mata:
        model=AuthUser
        fields=['username','email','password']
        extra_kwargs = {"password": {"write_only": True}}
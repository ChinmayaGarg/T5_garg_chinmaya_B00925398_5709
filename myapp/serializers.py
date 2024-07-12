from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='first_name')

    class Meta:
        model = User
        fields = ['id', 'email', 'firstName']

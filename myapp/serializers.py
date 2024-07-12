from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='first_name')

    class Meta:
        model = User
        fields = ['id', 'email', 'firstName']

    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        user = User.objects.create(first_name=first_name, **validated_data)
        return user

from rest_framework import serializers
from app.models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields=(
            'id',
            'name',
            'identification',
            'address',
            'phone',
            'email'
        )
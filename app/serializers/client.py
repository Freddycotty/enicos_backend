from rest_framework import serializers
from app.models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields=(
            'id',
            'name',
            'lastname',
            'identification',
            'identification_type',
            'address',
            'phone',
            'email'
        )
        extra_kwargs = {
            'identification': {'validators': []},
            'email': {'validators': []},
        }
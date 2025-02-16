from rest_framework import serializers
from app.models import Suppiler

class SuppilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppiler
        fields = (
            'id',
            'name',
            'email',
            'phone',
            'is_active'
        )
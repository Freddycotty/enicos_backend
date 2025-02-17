from rest_framework import serializers
from app.models.base import IdentificationType


class IdentificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentificationType
        fields = (
            'id',
            'name',
            'code',
            'is_active'
        )
        read_only_fields = ('is_active',)

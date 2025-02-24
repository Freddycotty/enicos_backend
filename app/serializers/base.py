from rest_framework import serializers
from app.models.base import (
    CurrencyRate,
    IdentificationType
)


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


class CurrencyRateSerializer(serializers.ModelSerializer):
    currency_name = serializers.CharField(source ='currency.name', read_only=True)
    class Meta:
        model = CurrencyRate
        fields = (
            'id',
            'amount',
            'date',
            'currency',
            'currency_name',
        )

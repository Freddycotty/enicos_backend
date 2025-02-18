from rest_framework import serializers
from app.models import PaymentMethod


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model= PaymentMethod
        fields=(
            'id',
            'name',
            'description',
            'is_active',
        )
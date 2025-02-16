from rest_framework import serializers
from app.models import Sales

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = (
            'id',
            'client',
            'date',
            'total',
            'payment_method',
            'seller'
        )

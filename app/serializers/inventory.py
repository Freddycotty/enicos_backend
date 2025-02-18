from rest_framework import serializers
from app.models.inventory import Inventory
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
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'id',
            'product_value',
            'quantity',
            'status',
            'transaction_type',
            'transaction_date',
            'transaction_reference',
            'user'
        ]

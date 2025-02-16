from rest_framework import serializers
from app.models.inventory import Inventory

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

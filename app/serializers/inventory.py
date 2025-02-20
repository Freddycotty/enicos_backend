from rest_framework import serializers
from app.models.inventory import Inventory
from app.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
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
            'supplier',
            'user'
        ]

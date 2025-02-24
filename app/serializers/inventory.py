from rest_framework import serializers
from app.models.inventory import (
    Supplier,
    Inventory,
    TransactionTypeInventory,
)


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
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    product_name= serializers.CharField(source='product_value.product.name', read_only=True)
    transaction_type_name = serializers.CharField(source='transaction_type.name', read_only=True)

    class Meta:
        model = Inventory
        fields = [
            'id',
            'product_name',
            'product_value',
            'quantity',
            'status',
            'transaction_type',
            'transaction_type_name',
            'supplier',
            'created_by',
            'created_by_name',
        ]
        extra_kwargs = {
            'created_by': {'write_only': True}
        }


class TransactionTypeInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionTypeInventory
        fields = [
            'id',
            'name',
            'is_active',
        ]

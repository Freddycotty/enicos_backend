from rest_framework import serializers
from app.models import (
    SaleDetail,
    Sales)

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

class SaleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetail
        fields = (
            'id',
            'sale_id',
            'product_value_id',
            'quantity',
            'unit_price'
        )

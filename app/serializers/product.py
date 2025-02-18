from rest_framework import serializers
from app.models import Product
from app.models import ProductValue

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name', 
            'description',
            'category',
            'supplier',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class ProductValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductValue
        fields = (
            'id',
            'price',
            'cost',
            'product_id'
        )

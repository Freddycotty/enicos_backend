from rest_framework import serializers
from app.models.product import ProductValue

class ProductValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductValue
        fields = (
            'id',
            'price',
            'cost',
            'product_id'
        )

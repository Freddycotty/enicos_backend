from rest_framework import serializers
from app.models import Product

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

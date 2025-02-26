from rest_framework import serializers
from app.models import Category

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'description',
            'parent',
            'is_active',
        )
        

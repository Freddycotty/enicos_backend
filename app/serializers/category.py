from rest_framework import serializers
from app.models import Category

class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=False,
        allow_null=True
    )
    
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'description',
            'parent_id',
            'is_active',
            'full_path'
        )
        

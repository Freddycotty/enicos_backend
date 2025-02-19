from rest_framework import serializers
from app.models import Product
from app.models import ProductValue


class ProductValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductValue
        fields = (
            'id',
            'price',
            'cost',
            'product_id'
        )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not (hasattr(self, 'context')):
            return

        create_product = self.context.get('create_product')
        
        if create_product:
            read_only_fields = ['product_id']
            for _field in read_only_fields:
                self.fields[_field].read_only = True



class ProductSerializer(serializers.ModelSerializer):
    value = ProductValueSerializer(write_only=True,context={'create_product': True})
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name', 
            'description',
            'subcategory',
            'value',
            'current_value',
            'created_at',
            'updated_at',
            'created_by',
        ]
        extra_kwargs = {
            'created_by': {'write_only': True},
        }

    def create(self, validated_data):
        # obtniendo el valor del producto
        value_data = validated_data.pop('value', None)
        if not value_data:
            raise serializers.ValidationError({'message':'Se requiere el valor del producto'})
        
        # registrando producto
        product = self.Meta.model.objects.create(**validated_data)

        # registrando valor del producto
        ProductValue.objects.create(product=product, **value_data)
        
        return product
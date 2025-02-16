from rest_framework import serializers
from app.models.sale_detail import SaleDetail

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

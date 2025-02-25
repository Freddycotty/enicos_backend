from rest_framework import serializers
from app.models import PaymentMethod, Bank, Payment, PaymentSaleDetail


class PaymentMethodSerializer(serializers.ModelSerializer):
    # Se agrega el nombre de la moneda asociada para lectura
    currency_name = serializers.CharField(source='currency.name', read_only=True)
    
    class Meta:
        model = PaymentMethod
        fields = (
            'id',
            'name',
            'description',
            'is_active',
            'currency',
            'currency_name',
        )

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = (
            'id',
            'achronym',
            'code',
            'name',
        )

class PaymentSerializer(serializers.ModelSerializer):
    # campos de solo lectura para mostrar información descriptiva de los bancos y metodos
    bank_origin_name = serializers.CharField(source='bank_origin.name', read_only=True)
    bank_destiny_name = serializers.CharField(source='bank_destiny.name', read_only=True)
    method_name = serializers.CharField(source='method.name', read_only=True)
    
    class Meta:
        model = Payment
        fields = (
            'id',
            'bank_origin',
            'bank_origin_name',
            'bank_destiny',
            'bank_destiny_name',
            'method',
            'method_name',
            'amount',
            'date',
            'description',
            'reference',
            'status',
            'created_at',
            'updated_at',
            'created_by',
        )
        extra_kwargs = {
            'created_by': {'write_only': True},
        }

class PaymentSaleDetailSerializer(serializers.ModelSerializer):
    # Se agregan campos descriptivos para facilitar la consulta
    payment_reference = serializers.CharField(source='payment.reference', read_only=True)
    sale_detail_id = serializers.IntegerField(source='sale_detail.id', read_only=True)
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = PaymentSaleDetail
        fields = (
            'id',
            'sale_detail',
            'sale_detail_id',
            'payment',
            'payment_reference',
            'amount',
            'created_at',
            'created_by',
            'created_by_name',
        )
        extra_kwargs = {
            'created_by': {'write_only': True},
        }
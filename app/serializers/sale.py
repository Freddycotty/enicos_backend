from rest_framework import serializers
import datetime
from app.models import (
    Sales,
    Client,
    SaleDetail,
    CurrencyRate,
)
from app.serializers.base import (
    CurrencyRateSerializer,
)
from app.serializers.client import (
    ClientSerializer,
)
from app.serializers.product import (
    ProductValueSerializer,
)


class SalesSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    client_name = serializers.CharField(source='client.name', read_only=True)
    currency_rate_amount = serializers.SerializerMethodField()  # Nueva propiedad para la tasa

    class Meta:
        model = Sales
        fields = (
            'id',
            'client',
            'client_name',
            'debt',
            'debt_bs',
            'currency_rate',
            'currency_rate_amount',
            'created_by',
            'created_by_name',
        )
        extra_kwargs = {
            'created_by': {'write_only': True}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not (hasattr(self, 'context')):
            return

        request = self.context.get('request')
        retrieve = self.context.get('retrieve')
        
        if request.method in ['POST']:
            self.fields['client'] = ClientSerializer()
            self.fields['sale_details'] = SaleDetailSerializer(many=True, context={"create_sale": True})
        if retrieve:
            self.fields['client'] = ClientSerializer()
            self.fields['currency_rate'] = CurrencyRateSerializer()
            self.fields['sale_details'] = SaleDetailSerializer(many=True, context={"retrieve": True})
            
            pop_fields = ['client_name']
            for _field in pop_fields:
                self.fields.pop(_field)

            
            

    def create(self, validated_data):
        # obtniendo los datos del cliente
        data_client = validated_data.pop('client', None)
        sale_details = validated_data.pop('sale_details', None)


        if not data_client:
            raise serializers.ValidationError({'message':'Se requiere datos del cliente'})
        try:
            client = Client.objects.get(
                identification_type=data_client['identification_type'],
                identification=data_client['identification'],
            )
        except Client.DoesNotExist:
            client = Client.objects.create(created_by=validated_data['created_by'], **data_client)
        except Exception as e:
            return serializers.ValidationError({"message": "Error al registrar informacion del cliente"})

        # registrando venta
        sale = self.Meta.model.objects.create(client=client, **validated_data)

        # registrando detalles de la venta
        for sale_detail in sale_details:
            SaleDetail.objects.create(sale=sale, created_by=sale.created_by, **sale_detail)

        return sale

    def get_currency_rate_amount(self, obj):
        currency_rate = obj.currency_rate

        # Si no tiene tasa, obtener la última tasa disponible del día actual
        if not currency_rate:
            currency_rate = CurrencyRate.objects.filter(date=datetime.date.today()).first()

        return currency_rate.amount if currency_rate else None  # Retorna None si no hay tasa

class SaleDetailSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = SaleDetail
        fields = (
            'id',
            'sale',
            'product_value',
            'quantity',
            "inventory",
            'created_by',
            'created_by_name',
        )
        extra_kwargs = {
            'created_by': {'write_only': True}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not (hasattr(self, 'context')):
            return

        create_sale = self.context.get('create_sale')
        retrieve = self.context.get('retrieve')
        
        if create_sale:
            pop_fields = ['sale']
            for _field in pop_fields:
                self.fields.pop(_field)

        if retrieve:
            self.fields['product_value'] = ProductValueSerializer(read_only=True)

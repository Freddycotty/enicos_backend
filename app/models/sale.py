from django.utils.translation import gettext_lazy as _
from django.db import models
from decimal import Decimal
import datetime
from django.db.models import (
    F,
    Sum,
    DecimalField
)
from app.models.client import Client
from app.models.base import BaseModel, CurrencyRate
from app.models.product import ProductValue
from app.models.inventory import Inventory


class Sales(BaseModel):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name='Cliente',
        help_text='Cliente asociado a la venta'
    )
    currency_rate = models.ForeignKey(
        CurrencyRate,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Currency Rate',
        help_text='Currency Rate'
    )


    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'sales'
        ordering = ('-created_at',)
        permissions = (
            ('list_sales', _('Can list Sales')),
        )

    @property
    def debt(self):
        total = self.sale_details.aggregate(
            total=Sum(F('product_value__price') * F('quantity'), output_field=DecimalField())
        )['total'] or 0

        subtotal = total / Decimal("1.16")  # Asumiendo que el total ya incluye el IVA
        iva = total - subtotal

        return {
            'subtotal': round(subtotal, 2),
            'iva': round(iva, 2),
            'total': round(total, 2)
        }

    @property
    def debt_bs(self):
        data = {
            "subtotal": None,
            "iva": None,
            "total": None
        }

        # Usar la tasa de cambio asignada en la venta si existe
        currency_rate = self.currency_rate

        # Si no hay tasa asignada, obtener la última disponible del día actual
        if not currency_rate:
            currency_rate = CurrencyRate.objects.filter(date=datetime.date.today()).first()


        if currency_rate:
            debt = self.debt

            data['subtotal'] = debt['subtotal'] * currency_rate.amount 
            data['iva'] = debt['iva'] * currency_rate.amount 
            data['total'] = debt['total'] * currency_rate.amount 
        return data
    


class SaleDetail(BaseModel):
    sale = models.ForeignKey(
        Sales,
        on_delete=models.CASCADE,
        verbose_name='Venta',
        help_text='Venta asociada',
        related_name='sale_details'
    )
    product_value = models.ForeignKey(
        ProductValue,
        on_delete=models.CASCADE,
        verbose_name='Valor del Producto',
        help_text='Valor del producto en el momento de la venta',
        related_name='sale_details'
    )
    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE,
        verbose_name='Valor del Producto',
        help_text='Valor del producto en el momento de la venta',
        related_name='sale_details'
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Cantidad',
        help_text='Cantidad de productos vendidos'
    )


    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Venta'
        db_table = 'sale_details'

    
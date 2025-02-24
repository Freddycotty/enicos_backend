from django.utils.translation import gettext_lazy as _
from django.db import models
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

    
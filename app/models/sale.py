from django.db import models
from app.models.user import User
from app.models.client import Client
from app.models.base import BaseModel
from app.models.product import ProductValue


class Sales(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name='Cliente',
        help_text='Cliente asociado a la venta'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha',
        help_text='Fecha de la venta'
    )
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Vendedor',
        help_text='Usuario que realizó la venta'
    )

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'sales'
        ordering = ('-date',)


class SaleDetail(BaseModel):
    sale_id = models.ForeignKey(
        Sales,
        on_delete=models.CASCADE,
        verbose_name='Venta',
        help_text='Venta asociada'
    )
    product_value_id = models.ForeignKey(
        ProductValue,
        on_delete=models.CASCADE,
        verbose_name='Valor del Producto',
        help_text='Valor del producto en el momento de la venta'
    ) 
    quantity = models.PositiveIntegerField(
        verbose_name='Cantidad',
        help_text='Cantidad de productos vendidos'
    )


    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Venta'
        db_table = 'sale_details'

    
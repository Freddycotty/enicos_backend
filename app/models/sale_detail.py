from django.db import models
from app.models.sale import Sales
from app.models.product_value import ProductValue

class SaleDetail(models.Model):
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
    
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Precio Unitario',
        help_text='Precio unitario del producto'
    )

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Venta'
        db_table = 'sale_details'

    
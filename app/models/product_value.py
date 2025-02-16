from django.db import models
from app.models.product import Product

class ProductValue(models.Model):
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Precio',
        help_text='Precio del producto'
    )
    
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Costo',
        help_text='Costo del producto'
    )
    
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Producto',
        help_text='Producto asociado a este valor'
    )

    class Meta:
        verbose_name = 'Valor del Producto'
        verbose_name_plural = 'Valores de Productos'
        db_table = 'product_values'

    
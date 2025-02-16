from django.db import models
from app.models.product_value import ProductValue
from app.models.user import User

class Inventory(models.Model):
    TRANSACTION_TYPES = [
        ('IN', 'Entrada'),
        ('OUT', 'Salida'),
    ]

    STATUS_CHOICES = [
        ('P', 'Pendiente'),
        ('C', 'Completado'),
        ('X', 'Cancelado'),
    ]

    product_value = models.ForeignKey(
        ProductValue,
        on_delete=models.CASCADE,
        verbose_name='Valor del Producto',
        help_text='Valor del producto relacionado'
    )
    
    quantity = models.IntegerField(
        verbose_name='Cantidad',
        help_text='Cantidad de productos'
    )
    
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        verbose_name='Estado',
        help_text='Estado de la transacción'
    )
    
    transaction_type = models.CharField(
        max_length=3,
        choices=TRANSACTION_TYPES,
        verbose_name='Tipo de Transacción',
        help_text='Tipo de transacción (Entrada/Salida)'
    )
    
    transaction_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de Transacción',
        help_text='Fecha de la transacción'
    )
    
    transaction_reference = models.CharField(
        max_length=255,
        verbose_name='Referencia de Transacción',
        help_text='Referencia o número de la transacción'
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Usuario',
        help_text='Usuario que realizó la transacción'
    )

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        db_table = 'inventory'

    

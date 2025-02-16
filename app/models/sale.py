from django.db import models
from app.models.user import User
from app.models.client import Client
from app.models.payment_method import PaymentMethod

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
    
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Total',
        help_text='Monto total de la venta'
    )
    
    payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.CASCADE,
        verbose_name='Método de pago',
        help_text='Método de pago utilizado'
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

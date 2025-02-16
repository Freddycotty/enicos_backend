from django.db import models
from app.models.user import User

class Sales(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='id_username',
        help_text='usuario asociando a la venta'
    )
    sale_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='fecha de la venta',
        help_text='fecha de la venta'
    )
    total_amount = models.DecimalField(
        decimal_places=2,
        verbose_name='Monto total',
        help_text='Monto total de la venta'
    )
    payment_method_id = models.ForeignKey(              
        pay
        on_delete=models.CASCADE,
        max_length=50,
        verbose_name='Método de pago',
        help_text='Método de pago utilizado')(
        
    )
    is_completed = models.BooleanField(
        default=True,
        verbose_name='Completada',
        help_text='Indica si la venta fue completada'
    )

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'sales'
        ordering = ('-sale_date',)

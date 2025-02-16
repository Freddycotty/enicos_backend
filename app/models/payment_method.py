from django.db import models

class PaymentMethod(models.Model):
    name = models.CharField(
        verbose_name='Nombre',
        max_length=255,
        blank=False,
        help_text='Nombre del método de pago',
        unique=True
    )
    
    description = models.TextField(
        verbose_name='Descripción',
        blank=True,
        help_text='Descripción del método de pago'
    )

    is_active = models.BooleanField(
        verbose_name='Activo',
        default=True,
        help_text='Indica si el método de pago está activo'
    )

    class Meta:
        verbose_name = 'Metodo de pago'
        verbose_name_plural = 'Metodos de pago'
        db_table = 'payment_methods'
        ordering = ('-id',)
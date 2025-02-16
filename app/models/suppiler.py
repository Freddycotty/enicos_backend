from django.db import models

class Suppiler(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='proveedores',
        help_text='Nombre del proveedor',
        blank=False 
        )
    email = models.EmailField(
        max_length=255,
        verbose_name='Correo electrónico',
        help_text='Correo electrónico del proveedor',
        blank=False
        )
    phone = models.CharField(
        max_length=20,
        verbose_name='Teléfono',
        help_text='Teléfono del proveedor',
        blank=False
        )
    is_active = models.BooleanField(
        verbose_name='Activo',
        default=True,
        help_text='Indica si el método de pago está activo'
    )
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'suppilers'
        ordering = ('-id',)
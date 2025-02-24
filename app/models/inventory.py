from django.db import models
from app.models.product import ProductValue
from app.models.user import User
from app.models.base import BaseModel


class Supplier(models.Model):
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
        db_table = 'Suppliers'
        ordering = ('-id',)


class TransactionTypeInventory(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Tipo de transacción',
        help_text='Tipo de transacción'
    )
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Tipo de transacción de inventario'
        verbose_name_plural = 'Tipos de transacciones de inventario'
        db_table = 'transaction_type_inventory'
        

class Inventory(BaseModel):
    product_value = models.ForeignKey(
        ProductValue,
        on_delete=models.CASCADE,
        verbose_name='Valor del Producto',
        help_text='Valor del producto relacionado'
    )
    transaction_type = models.ForeignKey(
        TransactionTypeInventory,
        on_delete=models.CASCADE,
        verbose_name='Tipo de transaccion',
        help_text='Tipo de transaccion'
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Cantidad',
        help_text='Cantidad de productos'
    )
    status = models.BooleanField(
        max_length=1,
        default=True,
        verbose_name='Estado',
        help_text='Estado de la transacción',
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        verbose_name='Proveedor',
        related_name='products'
    )
    transaction_detail = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Detalles de la transaccion',
        help_text='Referencia o número de la transacción'
    )

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        db_table = 'inventory'
from django.db import models
from app.models.base import BaseModel
from app.models.category import Category


class Product(BaseModel):
    name = models.CharField(
        verbose_name='Nombre',
        max_length=255,
        blank=False,
        help_text='Nombre del producto'
    )
    description = models.TextField(
        verbose_name='Descripción',
        blank=True,
        help_text='Descripción detallada del producto'
    )
    # TODO: Relation only with Subcategory
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Categoría',
        related_name='products'
    )
    created_at = models.DateTimeField(
        verbose_name='Fecha de creación',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Fecha de actualización', 
        auto_now=True
    )

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['name']


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

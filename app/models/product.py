from django.db import models
from app.models.category import Category
from app.models.suppiler import Suppiler

class Product(models.Model):
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
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Categoría',
        related_name='products'
    )
    
    supplier = models.ForeignKey(
        Suppiler,  
        on_delete=models.CASCADE,
        verbose_name='Proveedor',
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

    
from django.utils.translation import gettext as _
from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name='Nombre',
        max_length=255,
        # unique=True,
        blank=False,
        help_text=_('Category name')
    )
    description = models.TextField(
        verbose_name='Descripción',
        blank=True,
        help_text='Descripción detallada de la categoría'
    )
    parent_id = models.ForeignKey(
        'self',
        verbose_name='Categoría padre',
        null=True,
        on_delete=models.SET_NULL,
        related_name='children',
        help_text='Categoría superior en la jerarquía'
    )
    is_active = models.BooleanField(
        verbose_name='Activa',
        default=True,
        help_text='Indica si la categoría está activa'
    )

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        db_table = 'categories'
        ordering = ('name',)
        unique_together = ['name', 'parent_id']
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=['name', 'parent_id'],
        #         name='unique_category_name_per_parent'
        #     )
        # ]

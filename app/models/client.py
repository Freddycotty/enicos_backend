from django.db import models
from app.models.base import BaseModel
from app.models.base import (
    IdentificationType
) 

class Client(BaseModel):
    name= models.CharField(
        verbose_name='name',
        max_length=255,
        blank=False,
        help_text='Nombre del cliente'
    )
    lastname= models.CharField(
        verbose_name='name',
        max_length=255,
        blank=False,
        help_text='Apellido del cliente'
    )
    identification = models.CharField(
        max_length=15,
        unique=True,
        blank=False,
        verbose_name='identification',
    )
    identification_type = models.ForeignKey(
        IdentificationType,
        verbose_name='identification type',
        on_delete=models.CASCADE,
        related_name='clients',
        help_text='Tipo de identificacion'
    )
    address= models.CharField(
        verbose_name='address',
        max_length=255,
        null=True,
        blank=False,
        help_text='Direccion'
    )
    phone = models.CharField(
        verbose_name='phone',
        max_length=255,
        null=True,
        blank=False,
        help_text='Numero de telefono',
    )
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
        blank=False,
        help_text='Correo electronico',
    )
    
    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
        db_table = 'clients'
        ordering = ('-id',)

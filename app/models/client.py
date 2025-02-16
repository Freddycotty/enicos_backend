from django.db import models

class Client(models.Model):
    name= models.CharField(
        verbose_name='name',
        max_length=255,
        null=True,
        blank=False,
        help_text='Nombre del cliente'
        )
    identification = models.CharField(
        max_length=15,
        unique=True,
        blank=False,
        verbose_name='identification',
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
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
        db_table = 'clients'
        ordering = ('-id',)

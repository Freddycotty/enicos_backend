from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    Permission,
    Group,
)
from app.models.managers import (
    UserManager,
)
# from app.models import (
#     Menus,
# )


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        blank=False,
        unique=True,
        help_text='Username',
    )
    name = models.CharField(
        verbose_name='name',
        max_length=255,
        blank=False,
        help_text='Nombre',
    )
    lastname = models.CharField(
        verbose_name='lastname',
        max_length=255,
        null=True,
        blank=False,
        help_text='Apellido',
    )
    #identification no deberia ser intfield
    identification = models.CharField(
        max_length=15,
        unique=True,
        blank=False,
        verbose_name='identification',
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
    is_staff = models.BooleanField(default=False)
    objects = UserManager()


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'users'
        ordering = ('-id',)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'lastname']

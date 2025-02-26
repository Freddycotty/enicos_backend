from simple_history.models import HistoricalRecords
from django.db import models


class BaseModel(models.Model):
    """
    Base Model
    """
    id = models.BigAutoField(
        primary_key=True,
        editable=False,
        help_text='ID único para la instancia del modelo.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        null=True,
        help_text='Fecha de creación del objeto',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        help_text='Fecha de actualización del objeto'
    )
    created_by = models.ForeignKey(
        'app.User',
        on_delete=models.CASCADE,
        related_name='+',
        null=True
    )
    updated_by = models.ForeignKey(
        'app.User',
        on_delete=models.CASCADE,
        related_name='+',
        null=True
    )
    historical = HistoricalRecords(user_model="app.User", inherit=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        abstract = True


class IdentificationType(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Tipo de identificación',
        help_text='Tipo de identificación'
    )
    code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Codigo del tipo de identificación',
        help_text='Codigo del tipo de identificación'
    )
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Tipo de identificación'
        verbose_name_plural = 'Tipos de identificaciones'
        db_table = 'identification_types'
        ordering = ('name',)


class Currency(models.Model):
    code = models.CharField(
        max_length=50
    )
    name = models.CharField(
        max_length=50
    )
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'currency'
        verbose_name_plural = 'currencys'
        db_table = 'currency'


class CurrencyRate(models.Model):
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        null=True,
        related_name='dollar_rate',
        help_text='Moneda',
    )
    date = models.DateField(
        auto_now_add=True
    )
    amount = models.DecimalField(
        max_digits=20,
        decimal_places=2
    )
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'currency rate'
        verbose_name_plural = 'currency rate'
        db_table = 'currency_rate'
        unique_together = ('currency', 'date')
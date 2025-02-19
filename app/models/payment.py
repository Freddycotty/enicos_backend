from django.db import models
from app.models.base import BaseModel, Currency
from app.models.sale import SaleDetail


# metodos de pagos
class PaymentMethod(models.Model):
    name = models.CharField(
        verbose_name='Nombre',
        max_length=255,
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
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        help_text='Moneda',
        related_name='payment_methods',
    )

    class Meta:
        verbose_name = 'Metodo de pago'
        verbose_name_plural = 'Metodos de pago'
        db_table = 'payment_methods'
        ordering = ('-id',)


# bancos
class Bank(models.Model):
    achronym = models.CharField(
        max_length=10,
        null=True,
        unique=True,
        help_text='Acronimo del banco'
    )
    code = models.CharField(
        max_length=10,
        null=False,
        unique=True,
        db_column='code',
        help_text='Codigo del banco'
    )
    name = models.CharField(
        max_length=100,
        help_text='Nombre del banco'
    )


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Bank'
        verbose_name_plural = 'Banks'
        db_table = 'banks'
        ordering = ('-id',)


# pagos
class Payment(BaseModel):
    bank_origin = models.ForeignKey(
        Bank,
        on_delete=models.CASCADE,
        help_text='Banco',
        related_name='origin_payments',
    )
    bank_destiny = models.ForeignKey(
        Bank,
        on_delete=models.CASCADE,
        help_text='Banco',
        related_name='distiny_payments',
    )
    method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.CASCADE,
        help_text='Método de pago',
        related_name='payment_company'
    )
    amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text='Monto del pago',
    )
    date = models.DateTimeField(
        auto_now_add=False,
        help_text='Fecha en la que se registro el pago',
    )
    description = models.TextField(
        blank=True,
        help_text='motivo/descripcion del pago'
    )
    reference = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        help_text='referencia de pagomovil/transferencia'
    )
    status = models.BooleanField(
        default=True
    )


    def __str__(self) -> str:
        return str(self.pk)


    class Meta:
        db_table = 'payments_company'
        unique_together = ('method', 'bank_destiny', 'reference','status')
        ordering = ('-id',)


# pagos-ventas
class PaymentSaleDetail(BaseModel):
    sale_detail = models.ForeignKey(
        SaleDetail,
        on_delete=models.CASCADE,
        related_name='payment_sale_detail',
        help_text='Id Factura del contrato',
    )
    payment = models.ForeignKey(
        Payment,
        on_delete=models.CASCADE,
        help_text='pago ligado a la factura',
        related_name='payment_sale_detail'
    )
    amount = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        help_text='Monto del pago',
    )

    def __str__(self) -> str:
        return str(self.amount)

    class Meta:
        verbose_name = 'Payment Sale Detail'
        verbose_name_plural = 'Payment Sale Details'
        db_table = 'payments_sale_details'
        ordering = ('-id',)

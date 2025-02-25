from django.urls import path
from app.apis.payment import (
    PaymentMethodLC,
    PaymentMethodRUD,
    BankLC,
    BankRUD,
    PaymentLC,
    PaymentRUD,
    PaymentSaleDetailLC,
)

urlpatterns = [
    # metodos de pago
    path("methods/", PaymentMethodLC.as_view(), name="payment-method-lc"),
    path("methods/<int:id>/", PaymentMethodRUD.as_view(), name="payment-method-rud"),

    # bancos
    path("banks/", BankLC.as_view(), name="bank-lc"),
    path("banks/<int:id>/", BankRUD.as_view(), name="bank-rud"),

    # pagos
    path("", PaymentLC.as_view(), name="payment-lc"),
    path("<int:id>/", PaymentRUD.as_view(), name="payment-rud"),

    # detalles de pago-venta
    path("sale-details/", PaymentSaleDetailLC.as_view(), name="payment-sale-detail-lc"),
]

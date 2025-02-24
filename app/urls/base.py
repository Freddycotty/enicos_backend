from django.urls import path
from app.apis import (
    IdentificationTypeLC,
    CurrencyRateLC,
)

urlpatterns = [
    path(
        'identification_type/',
        IdentificationTypeLC.as_view(),
        name='identification_type'
    ),
    path(
        'currency_rate/',
        CurrencyRateLC.as_view(),
        name='currency_rate'
    ),
]

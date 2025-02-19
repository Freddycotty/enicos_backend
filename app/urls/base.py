from django.urls import path
from app.apis import (
    IdentificationTypeLC,
)

urlpatterns = [
    path(
        'identification_type/',
        IdentificationTypeLC.as_view(),
        name='identification_type'
    )
]

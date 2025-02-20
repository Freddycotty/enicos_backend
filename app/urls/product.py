from django.urls import path
from app.apis import (
    ProductLC,
)

urlpatterns = [
    path(
        '',
        ProductLC.as_view(),
        name='product'
    ),
]

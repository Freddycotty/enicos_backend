from django.urls import path
from app.apis import (
    ProductLC,
    ProductRUD,
    ProductValueLC,
)

urlpatterns = [
    path(
        '',
        ProductLC.as_view(),
        name='product-lc'
    ),
    path(
        '<int:id>/',
        ProductRUD.as_view(),
        name='product-rud'
    ),
    path(
        'values/',
        ProductValueLC.as_view(),
        name='product_value-lc'
    ),
]

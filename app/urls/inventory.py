from django.urls import path
from rest_framework.routers import DefaultRouter
from app.apis import (
    InventoryLC,
    InventoryRUD,
    SupplierMV,
    TransactionTypeInventoryL,
)


router = DefaultRouter()

router.register('suppliers', SupplierMV, basename='suppliers')

urlpatterns = [
    path('', InventoryLC.as_view(), name='inventory-lc'),
    path('<int:pk>/', InventoryRUD.as_view(), name='inventory-rud'),
    path('transaction_types/', TransactionTypeInventoryL.as_view(), name='transaction_type-l'),
]
urlpatterns += router.urls
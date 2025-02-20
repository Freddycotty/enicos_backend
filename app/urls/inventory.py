from django.urls import path
from app.apis.inventory import (
    InventoryLC,
    InventoryRUD,
)

urlpatterns = [
    path('', InventoryLC.as_view(), name='inventory-lc'),
    path('<int:pk>/', InventoryRUD.as_view(), name='inventory-rud'),
]

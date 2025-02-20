from django.urls import path
from rest_framework.routers import DefaultRouter
from app.apis import (
    SupplierMV,
)
router = DefaultRouter()

router.register('', SupplierMV, basename='suppliers')

urlpatterns = []
urlpatterns += router.urls
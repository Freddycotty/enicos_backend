from django.urls import path
from rest_framework.routers import DefaultRouter
from app.apis import (
    SuppilerMV,
)
router = DefaultRouter()

router.register('', SuppilerMV, basename='suppliers')

urlpatterns = []
urlpatterns += router.urls
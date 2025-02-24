from django.urls import path
from rest_framework.routers import DefaultRouter
from app.apis import (
    SaleMV,
)


router = DefaultRouter()

router.register('', SaleMV, basename='sales')

urlpatterns = []
urlpatterns += router.urls
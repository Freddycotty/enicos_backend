from django.urls import path
from app.apis import (
    CategoryLC,
    CategoryRUD,
)

urlpatterns = [
    path(
        '',
        CategoryLC.as_view(),
        name='category'
    ),
    path(
        '<int:pk>/',
        CategoryRUD.as_view(),
        name='category'
    )
]

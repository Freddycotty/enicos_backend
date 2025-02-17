from django.contrib import admin
from django.urls import (
    path,
    include,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from app.apis.authentication import (
    Login,
    Logout,
)
urlpatterns = [
    path(
        'login/',
        Login.as_view(),
        name='login'
    ),
    path(
        'logout/',
        Logout.as_view(),
        name='logout'
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(),
        name='redoc'
    ),
    path(
        'api/schema/',
        SpectacularAPIView.as_view(),
        name='schema'
    ),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(),
        name='swagger'
    ),
    path(
        'api/',
        include(
            (
                'app.urls',
                'app'
            ),
            namespace='api'
        ),
    )
]

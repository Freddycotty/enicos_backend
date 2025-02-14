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
# from app.apis import (
#     Login,
#     Logout,
#     LoginPortal,
#     RefreshToken,
#     LogoutPortal,
#     ForgotPassword,
# )
urlpatterns = [
    path(
        'api/admin/',
        admin.site.urls
    ),
    # path(
    #     'login/',
    #     Login.as_view(),
    #     name='login'
    # ),
    # path(
    #     'logout/',
    #     Logout.as_view(),
    #     name='logout'
    # ),
    # path(
    #     'portal/login/',
    #     LoginPortal.as_view(),
    #     name='login_portal'
    # ),
    # path(
    #     'portal/logout/',
    #     LogoutPortal.as_view(),
    #     name='logout_portal'
    # ),
    # path(
    #     'portal/forgot_password/',
    #     ForgotPassword.as_view(),
    #     name='forgot_password'
    # ),
    # path(
    #     'refresh/',
    #     RefreshToken.as_view(),
    #     name='refresh'
    # ),
    path(
        'api/schema/',
        SpectacularAPIView.as_view(),
        name='schema'
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(),
        name='redoc'
    ),
    # path(
    #     'api/swagger/',
    #     SpectacularSwaggerView.as_view(),
    #     name='swagger'
    # ),
    # path(
    #     'api/',
    #     include(
    #         (
    #             'app.urls',
    #             'app'
    #         ),
    #         namespace='api'
    #     ),
    # )
]

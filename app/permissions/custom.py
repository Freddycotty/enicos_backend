from django.http import HttpResponseForbidden
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, BasePermission
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsSelf(IsAuthenticated):
    """
    Permission class to check if the object is the same as the requester is.
    """

    def has_permission(self, request, view):
        return super().has_permission(request, view) and view.is_self


class HasModelPermission(IsAuthenticated):
    ALLOWED_METHODS = ['ALL', 'GET', 'PUT', 'PATCH', 'OPTIONS', 'HEAD', 'DELETE', 'POST']

    def set_permissions(self, permissions=None):
        if permissions is None:
            permissions = {}

        self.model_permissions = {
            method: permissions.get(method, []) + permissions.get('ALL', [])
            for method in self.ALLOWED_METHODS
        }

    def has_permission(self, request, view):
        self.set_permissions(getattr(view, 'model_permissions', {}))
        return super().has_permission(request, view) and request.user.has_perms(self.model_permissions.get(request.method, []))


def method_permission_classes(classes):
    def decorator(func):
        def decorated_func(self, *args, **kwargs):
            self.permission_classes = classes
            # this call is needed for request permissions
            self.check_permissions(self.request)
            return func(self, *args, **kwargs)
        return decorated_func
    return decorator


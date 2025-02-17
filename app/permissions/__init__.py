from app.permissions.custom import (    # noqa: F401
    ReadOnly,
    HasModelPermission,
    method_permission_classes,
    IsSelf,
)
from app.permissions.schema import CustomJWTAuthenticationScheme
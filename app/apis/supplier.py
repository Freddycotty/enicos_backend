from rest_framework import (
    status,
    filters,
    viewsets,
    generics,
    permissions,
)
from rest_framework.response import (
    Response,
)
from app.models import Suppiler
from app.serializers import SuppilerSerializer
from app.permissions import HasModelPermission
from django_filters.rest_framework import (
    DjangoFilterBackend,
)

from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    inline_serializer,
)
from app.mixins import (
    OptionalPaginationMixin,
)


# listar, consultar, crear, editar y eliminar un proveedor
class SuppilerMV(OptionalPaginationMixin, viewsets.ModelViewSet):
    lookup_field = 'uid'
    lookup_url_kwarg = 'uid'
    queryset = Suppiler.objects.all()
    serializer_class = SuppilerSerializer
    filter_backends = (
        filters.SearchFilter,
    )
    search_fields = (
        "name",
        "phone",
        "email",
    )
    permission_classes = [
        permissions.IsAdminUser
        |
        (HasModelPermission)
    ]
    model_permissions = {
        "GET": ["app.view_suppiler"],
        "POST": ["app.add_suppiler"],
        "PATCH": ["app.change_suppiler"],
        "PUT": ["app.change_suppiler"],
        "DELETE": ["app.delete_suppiler"],
    }

    @extend_schema(
        tags=["Inventory"],
        operation_id='Listar Proveedores',
        description="""Ruta para listar proveedores. Debe tener el permiso: `view_suppiler` o ser administrador.""",
        parameters=[
            OpenApiParameter(
                name="no_pagination",
                type=bool,
                location=OpenApiParameter.QUERY,
                required=False,
                description="Si se establece en 'true' o '1', la respuesta no estará paginada."
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=["Inventory"],
        operation_id='Consultar un proveedor',
        description="""Ruta para consultar un proveedor. Debe tener el permiso: `view_suppiler` o ser administrador.""",

    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=["Inventory"],
        operation_id='Crear "Proveedores"',
        description="""Ruta para crear Proveedores. Debe tener el permiso: `add_suppiler` o ser administrador.""",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=["Inventory"],
        operation_id='Actualizar Proveedor',
        description="""Ruta para actualizar un proveedor. Debe tener el permiso: `change_suppiler` o ser administrador.""",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=["Inventory"],
        operation_id='Modificar Proveedor',
        description="""Ruta para modificar parcialmente un proveedor. Debe tener el permiso: `change_suppiler` o ser administrador.""",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def destroy(self, request, pk=None):
        return Response(status=405)

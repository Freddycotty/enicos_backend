from rest_framework import (
    status,
    filters,
    generics,
    permissions,
)
from rest_framework.response import Response
from app.models.inventory import Inventory
from app.serializers.inventory import InventorySerializer
from app.permissions import HasModelPermission
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
)

class InventoryLC(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('product_value__product__name',)
    filterset_fields = ('status', 'transaction_type', 'supplier')
    permission_classes = [
        permissions.IsAdminUser | HasModelPermission
    ]
    model_permissions = {
        "GET": ["app.view_inventory"],
        "POST": ["app.add_inventory"],
    }

    @extend_schema(
        tags=["Inventory"],
        operation_id='Crear Inventario',
        description="""Ruta para crear registros de inventario. Requiere permiso: `add_inventory` o ser administrador.""",
    )
    def post(self, request, *args, **kwargs):
        request.data["user"] = request.user.pk
        return super().post(request, *args, **kwargs)

    @extend_schema(
        tags=["Inventory"],
        operation_id='Consultar Inventario',
        description="""Ruta para listar registros de inventario. Requiere permiso: `view_inventory` o ser administrador.""",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class InventoryRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [
        permissions.IsAdminUser | HasModelPermission
    ]
    model_permissions = {
        "GET": ["app.view_inventory"],
        "PUT": ["app.change_inventory"],
        "DELETE": ["app.delete_inventory"],
    }

    @extend_schema(
        tags=["Inventory"],
        operation_id='Actualizar Inventario',
        description="""Ruta para actualizar registros de inventario. Requiere permiso: `change_inventory` o ser administrador.""",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Inventory"],
        operation_id='Eliminar Inventario',
        description="""Ruta para eliminar registros de inventario. Requiere permiso: `delete_inventory` o ser administrador.""",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

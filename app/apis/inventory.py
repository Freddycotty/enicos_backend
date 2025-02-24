from rest_framework import (
    filters,
    viewsets,
    generics,
    permissions,
)
from rest_framework.response import Response
from app.models import (
    Supplier,
    Inventory,
    TransactionTypeInventory,
)
from app.serializers import (
    InventorySerializer,
    SupplierSerializer,
    TransactionTypeInventorySerializer,
)
from app.mixins import (
    OptionalPaginationMixin,
)
from app.permissions import (
    HasModelPermission,
)
from django_filters.rest_framework import (
    DjangoFilterBackend,
)
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


# listar, consultar, crear, editar y eliminar un proveedor
class SupplierMV(OptionalPaginationMixin, viewsets.ModelViewSet):
    lookup_field = 'uid'
    lookup_url_kwarg = 'uid'
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
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
        "GET": ["app.view_Supplier"],
        "POST": ["app.add_Supplier"],
        "PATCH": ["app.change_Supplier"],
        "PUT": ["app.change_Supplier"],
        "DELETE": ["app.delete_Supplier"],
    }

    @extend_schema(
        tags=["Inventory"],
        operation_id='Listar Proveedores',
        description="""Ruta para listar proveedores. Debe tener el permiso: `view_Supplier` o ser administrador.""",
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
        description="""Ruta para consultar un proveedor. Debe tener el permiso: `view_Supplier` o ser administrador.""",

    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=["Inventory"],
        operation_id='Crear "Proveedores"',
        description="""Ruta para crear Proveedores. Debe tener el permiso: `add_Supplier` o ser administrador.""",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=["Inventory"],
        operation_id='Actualizar Proveedor',
        description="""Ruta para actualizar un proveedor. Debe tener el permiso: `change_Supplier` o ser administrador.""",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=["Inventory"],
        operation_id='Modificar Proveedor',
        description="""Ruta para modificar parcialmente un proveedor. Debe tener el permiso: `change_Supplier` o ser administrador.""",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def destroy(self, request, pk=None):
        return Response(status=405)


class TransactionTypeInventoryL(generics.ListAPIView):
    queryset = TransactionTypeInventory.objects.all()
    serializer_class = TransactionTypeInventorySerializer
    permission_classes = [
        permissions.IsAdminUser | HasModelPermission
    ]
    model_permissions = {
        "GET": ["app.view_transactiontypeinventory"],
    }

    @extend_schema(
        tags=["Inventory"],
        operation="Listar Tipos de Transacciones de Inventario",
        description="Ruta para listar los tipos de transacciones de inventario. Requiere permiso: `view_transactiontypeinventory` o ser administrador.",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

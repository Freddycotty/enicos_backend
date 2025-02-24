from rest_framework import (
    filters,
    viewsets,
    generics,
    permissions,
)
from rest_framework.response import Response
from app.models import (
    Sales,
)
from app.serializers import (
    SalesSerializer,
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


# listar, consultar, modifica, eliminar y crear una venta
class SaleMV(viewsets.ModelViewSet):
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter
    )
    search_fields = (
        'client__name',
        'client__lastname',
        'client__identification',
    )
    filterset_fields = (
        'client',
        'created_by',
        'currency_rate',
    )
    permission_classes = [
        permissions.IsAdminUser
        |
        HasModelPermission
    ]
    model_permissions = {
        "GET": ["app.view_sales", "app.list_sales"],
        "POST": ["app.add_sales"],
        "PUT": ["app.change_sales"],
        "PATCH": ["app.change_sales"],
        "DELETE": ["app.delete_sales"],
    }

    def get_serializer_context(self):
        id = self.kwargs.get('id')
        context = super().get_serializer_context()
        
        if id:
            context['retrieve'] = True
        return context

    @extend_schema(
        tags=["Sales"],
        operation_id='Generar Venta',
        description="""Ruta para generar una venta. Requiere permiso: `add_sales` o ser administrador.""",
    )
    def create(self, request, *args, **kwargs):
        request.data["created_by"] = request.user.pk
        return super().create(request, *args, **kwargs)

    @extend_schema(
        tags=["Sales"],
        operation_id='Listar Ventas',
        description="""Ruta para listar ventas. Requiere permiso: `view_sales` o ser administrador.""",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        tags=["Sales"],
        operation_id='Consultar una venta',
        description="""Ruta para consular una venta. Requiere permiso: `view_sales` o ser administrador.""",
    )
    def retrieve(self, request, *args, **kwargs):
        print(id)
        return super().retrieve(request, *args, **kwargs)


    @extend_schema(
        tags=["Sales"],
        operation_id='Actualizar venta',
        description="""Ruta para actualizar una venta. Requiere permiso: `change_sales` o ser administrador.""",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=["Sales"],
        operation_id='Modificar venta',
        description="""Ruta para modificar una venta. Debe tener el permiso: `change_sales` o ser administrador.""",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=["Sales"],
        operation_id='Eliminar venta',
        description="""Ruta para eliminar una venta. Debe tener el permiso: `delete_sales` o ser administrador.""",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

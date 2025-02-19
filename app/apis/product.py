from rest_framework import (
    status,
    filters,
    generics,
    permissions,
)
from rest_framework.response import (
    Response,
)
from app.models import Product
from app.serializers import ProductSerializer
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


# listar y crear productos
class ProductLC(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )
    search_fields = (
        "name",
    )
    filterset_fields = (
        'subcategory',
    )
    permission_classes = [
        permissions.IsAdminUser
        |
        (HasModelPermission)
    ]
    model_permissions = {
        "GET": ["app.view_product"],
        "POST": ["app.add_product"],
    }


    @extend_schema(
        tags=["Product"],
        operation_id='Crear Producto',
        description="""Ruta para crear productos. Debe tener el permiso: `add_product` o ser administrador. 
        El campo `created_by` se establece automáticamente con el ID del usuario de la sesión.""",
    )
    def post(self, request, *args, **kwargs):
        request.data["created_by"] = request.user.pk
        return super().post(request, *args, **kwargs)


    @extend_schema(
        tags=["Product"],
        operation_id='Consultar Products',
        description="""Ruta para listar consultar productos. Debe tener el permiso: `view_product` o ser administrador.""",
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
    @extend_schema(tags=["Base"], operation_id='Listar "Tipos de documentacion"')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

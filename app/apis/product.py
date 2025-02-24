from rest_framework import (
    status,
    filters,
    generics,
    permissions,
    serializers,
)
from rest_framework.response import (
    Response,
)
from app.models import (
    Product,
    ProductValue,
)
from app.serializers import (
    ProductSerializer,
    ProductValueSerializer,
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

    def get_serializer_context(self):
        context = super().get_serializer_context()
        
        
        if self.request.method == 'POST':
            context['create_product'] = True
        

        return context

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


class ProductRUD(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'id'
    lookup_field = 'id'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        permissions.IsAdminUser
        |
        (HasModelPermission)
    ]
    model_permissions = {
        "GET": ["app.view_product"],
        "PUT": ["app.change_product"],
        "PATCH": ["app.change_product"],
        "DELETE": ["app.delete_product"],
    }
    
    @extend_schema(
        tags=["Product"],
        operation_id='Consultar un producto',
        description="""Ruta para consultar un producto. Requiere permiso: `view_product` o ser administrador.""",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Product"],
        operation_id="Modificar Producto",
        description="""Ruta para modificar parcialmente un producto. Requiere permiso: `change_product` o ser administrador."""
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        tags=["Product"],
        operation_id="Actualizar Producto",
        description="""Ruta para actualizar un producto. Requiere permiso: `change_product` o ser administrador.""",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Product"],
        operation_id="Eliminar producto",
        description="""Ruta para eliminar un producto. Requiere permiso: `delete_product` o ser administrador.""",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# listar, crear valores de productos
class ProductValueLC(OptionalPaginationMixin, generics.ListCreateAPIView):
    queryset = ProductValue.objects.all()
    serializer_class = ProductValueSerializer
    filter_backends = (
        DjangoFilterBackend,
    )
    filterset_fields = (
        "product",
    )
    permission_classes = [
        permissions.IsAdminUser
        |
        (HasModelPermission)
    ]
    model_permissions = {
        "GET": ["app.view_productvalue"],
        "POST": ["app.add_productvalue"],
    }

    @extend_schema(
        tags=["Product"],
        operation_id='Listar Valores de Producto',
        description="""Ruta para listar valores de productos. Debe tener el permiso: `view_productvalue` o ser administrador.""",
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
    def get(self, request, *args, **kwargs):
        product = self.request.query_params.get('product')
        if not product:
            return Response({"product": ["Este campo es requerido."]}, status=status.HTTP_400_BAD_REQUEST)
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Product"],
        operation_id='Crear Valor de Producto',
        description="""Ruta para crear valores de productos. Debe tener el permiso: `add_productvalue` o ser administrador.""",
        request=inline_serializer(
        name="Product values create",
        fields={
            "price": serializers.DecimalField(max_digits=10, decimal_places=2),
            "cost": serializers.DecimalField(max_digits=10, decimal_places=2),
            "product": serializers.IntegerField(default=1)
        }
    ))
    def post(self, request, *args, **kwargs):
        request.data['created_by'] = request.user.pk
        return super().post(request, *args, **kwargs)

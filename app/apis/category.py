from rest_framework import (
    status,
    filters,
    generics,
    permissions,
)
from rest_framework.response import (
    Response,
)
from app.models import Category
from app.serializers import CategorySerializer
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
from app.filters.category import (
    CategoryFilter
)


# listar y crear categorias y subcategorias
class CategoryLC(OptionalPaginationMixin, generics.ListCreateAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )
    search_fields = (
        "name",
    )
    filterset_class = CategoryFilter
    permission_classes = [
        permissions.IsAdminUser
        |
        (HasModelPermission)
    ]
    model_permissions = {
        "GET": ["app.view_category"],
        "POST": ["app.add_category"],
    }

    @extend_schema(
        tags=["Category"],
        operation_id='Crear "Categorias/Subcategorias"',
        description="""Ruta para crear categorias y subcategorias. Debe tener el permiso: `add_category` o ser administrador.""",

    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


    @extend_schema(
        tags=["Category"],
        operation_id='Consultar "Categorias/Subcategorias"',
        description="""Ruta para listar categorias/subcategorias. Debe tener el permiso: `view_category` o ser administrador.""",
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


# Consultar, actualizar y eliminar categorias y subcategorias
class CategoryRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        permissions.IsAdminUser
        |
        (HasModelPermission)
    ]
    model_permissions = {
        "GET": ["app.view_category"],
        "PATCH": ["app.change_category"],
        "DELETE": ["app.delete_category"],
    }

    @extend_schema(
        tags=["Category"],
        operation_id='Actualizar "Categorias/Subcategorias"',
        description="""Ruta para actualizar categorías y subcategorías. 
        Debe tener el permiso: `change_category` o ser administrador. 
        Para agregar subcategorías, envía una lista de IDs en `subcategories`. 
        Para eliminar subcategorías, envía una lista vacía `subcategories: []`.""",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def put(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


    @extend_schema(
        tags=["Category"],
        operation_id='Consultar "Categorias/Subcategorias"',
        description="""Ruta para consultar una categoría o subcategoría específica. 
        Debe tener el permiso: `view_category` o ser administrador.""",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Category"],
        operation_id='Eliminar "Categorias/Subcategorias"',
        description="""Ruta para eliminar una categoría o subcategoría específica. 
        Debe tener el permiso: `delete_category` o ser administrador.""",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

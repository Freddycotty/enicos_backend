from rest_framework import generics, permissions
from app.models import IdentificationType
from app.serializers import IdentificationTypeSerializer
from app.permissions import HasModelPermission
from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    inline_serializer,
)
from app.mixins import (
    OptionalPaginationMixin,
)


# ruta para listar y crear tipos de identificacion
class IdentificationTypeLC(OptionalPaginationMixin, generics.ListCreateAPIView):
    queryset = IdentificationType.objects.filter(is_active=True)
    serializer_class = IdentificationTypeSerializer
    permission_classes = [
        permissions.IsAdminUser
        |
        (HasModelPermission)
    ]
    model_permissions = {
        "GET": ["app.view_identificationtype"],
        "POST": ["app.add_identificationtype"],
    }


    @extend_schema(
        tags=["Base"],
        operation_id='Crear "Tipos de identificación"',
        description="""Ruta para crear tipos de identificacion. Debe tener el permiso: `add_identificationtype` o ser administrador.""",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        tags=["Base"],
        operation_id='Consultar "Tipos de identificación"',
        description="""Ruta para listar tipos de identificacion. Debe tener el permiso: `view_identificationtype` o ser administrador.""",
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

from rest_framework import generics, permissions
from app.models import IdentificationType
from app.serializers import IdentificationTypeSerializer
from app.permissions import HasModelPermission
from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    inline_serializer,
)



# ruta para listar y crear tipos de identificacion
class IdentificationTypeLC(generics.ListCreateAPIView):
    """
    Ruta para listar y crear tipos de identificaciones,
    debe ser administrador (`is_staff` es `True`)
    o tener el permiso:
    - `view_identificationtype` para GET,
    - `add_identificationtype` para POST,
    """

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


    @extend_schema(tags=["Base"], operation_id='Crear "Tipos de documentacion"')
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(tags=["Base"], operation_id='Listar "Tipos de documentacion"')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


# ruta para consultar, editar y eliminar tipos de identificacion
class IdentificationTypeLC(generics.RetrieveUpdateDestroyAPIView):
    # TODO: Implementar la vista para consultar, editar y eliminar tipos de identificacion
    pass
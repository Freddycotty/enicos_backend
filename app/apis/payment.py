from rest_framework import (
    generics,
    status,
    filters,
    permissions,
    serializers,
)
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    inline_serializer,
)
from app.models import PaymentMethod, Bank, Payment, PaymentSaleDetail
from app.serializers import (
    PaymentMethodSerializer,
    BankSerializer,
    PaymentSerializer,
    PaymentSaleDetailSerializer,
)
from app.permissions import HasModelPermission


# metodos de pago: listar y crear
class PaymentMethodLC(generics.ListCreateAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [permissions.IsAdminUser | HasModelPermission]
    model_permissions = {
        "GET": ["app.view_paymentmethod"],
        "POST": ["app.add_paymentmethod"],
    }

    @extend_schema(
        tags=["Payment"],
        operation_id="Listar Métodos de Pago",
        description="Ruta para listar métodos de pago. Requiere permiso `view_paymentmethod` o ser administrador.",
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
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Payment"],
        operation_id="Crear Método de Pago",
        description="Ruta para crear un método de pago. Requiere permiso `add_paymentmethod` o ser administrador.",
    )
    def post(self, request, *args, **kwargs):
        # Si se requiere asignar automáticamente el usuario creador:
        request.data["created_by"] = request.user.pk
        return super().post(request, *args, **kwargs)


# metodos de pago: detalle, actualizacion y eliminacion
class PaymentMethodRUD(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    lookup_url_kwarg = "id"
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [permissions.IsAdminUser | HasModelPermission]
    model_permissions = {
        "GET": ["app.view_paymentmethod"],
        "PUT": ["app.change_paymentmethod"],
        "PATCH": ["app.change_paymentmethod"],
        "DELETE": ["app.delete_paymentmethod"],
    }

    @extend_schema(
        tags=["Payment"],
        operation_id="Consultar Método de Pago",
        description="Ruta para consultar un método de pago. Requiere permiso `view_paymentmethod` o ser administrador.",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Payment"],
        operation_id="Actualizar Método de Pago",
        description="Ruta para actualizar un método de pago. Requiere permiso `change_paymentmethod` o ser administrador.",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Payment"],
        operation_id="Modificar Método de Pago",
        description="Ruta para modificar parcialmente un método de pago. Requiere permiso `change_paymentmethod` o ser administrador.",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        tags=["Payment"],
        operation_id="Eliminar Método de Pago",
        description="Ruta para eliminar un método de pago. Requiere permiso `delete_paymentmethod` o ser administrador.",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# Bancos: Listar y Crear
class BankLC(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [permissions.IsAdminUser | HasModelPermission]
    model_permissions = {
        "GET": ["app.view_bank"],
        "POST": ["app.add_bank"],
    }

    @extend_schema(
        tags=["Payment"],
        operation_id="Listar Bancos",
        description="Ruta para listar bancos. Requiere permiso `view_bank` o ser administrador.",
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
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Payment"],
        operation_id="Crear Banco",
        description="Ruta para crear un banco. Requiere permiso `add_bank` o ser administrador.",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


# Bancos: Detalle, Actualización y Eliminación
class BankRUD(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    lookup_url_kwarg = "id"
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [permissions.IsAdminUser | HasModelPermission]
    model_permissions = {
        "GET": ["app.view_bank"],
        "PUT": ["app.change_bank"],
        "PATCH": ["app.change_bank"],
        "DELETE": ["app.delete_bank"],
    }

    @extend_schema(
        tags=["Payment"],
        operation_id="Consultar Banco",
        description="Ruta para consultar un banco. Requiere permiso `view_bank` o ser administrador.",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Payment"],
        operation_id="Actualizar Banco",
        description="Ruta para actualizar un banco. Requiere permiso `change_bank` o ser administrador.",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Payment"],
        operation_id="Modificar Banco",
        description="Ruta para modificar parcialmente un banco. Requiere permiso `change_bank` o ser administrador.",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        tags=["Payment"],
        operation_id="Eliminar Banco",
        description="Ruta para eliminar un banco. Requiere permiso `delete_bank` o ser administrador.",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# pagos: listar y crear
class PaymentLC(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["reference", "description"]
    filterset_fields = ["bank_origin", "bank_destiny", "method", "status"]
    permission_classes = [permissions.IsAdminUser | HasModelPermission]
    model_permissions = {
        "GET": ["app.view_payment"],
        "POST": ["app.add_payment"],
    }

    @extend_schema(
        tags=["Payment"],
        operation_id="Listar Pagos",
        description="Ruta para listar pagos. Requiere permiso `view_payment` o ser administrador.",
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
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Payment"],
        operation_id="Crear Pago",
        description="Ruta para crear un pago. Requiere permiso `add_payment` o ser administrador.",
    )
    def post(self, request, *args, **kwargs):
        request.data["created_by"] = request.user.pk
        return super().post(request, *args, **kwargs)


# pagos: detalle, actualización y eliminación
class PaymentRUD(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    lookup_url_kwarg = "id"
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAdminUser | HasModelPermission]
    model_permissions = {
        "GET": ["app.view_payment"],
        "PUT": ["app.change_payment"],
        "PATCH": ["app.change_payment"],
        "DELETE": ["app.delete_payment"],
    }

    @extend_schema(
        tags=["Payment"],
        operation_id="Consultar Pago",
        description="Ruta para consultar un pago. Requiere permiso `view_payment` o ser administrador.",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Payment"],
        operation_id="Actualizar Pago",
        description="Ruta para actualizar un pago. Requiere permiso `change_payment` o ser administrador.",
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        tags=["Payment"],
        operation_id="Modificar Pago",
        description="Ruta para modificar parcialmente un pago. Requiere permiso `change_payment` o ser administrador.",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        tags=["Payment"],
        operation_id="Eliminar Pago",
        description="Ruta para eliminar un pago. Requiere permiso `delete_payment` o ser administrador.",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# Detalles de Pago-Venta: Listar y Crear
class PaymentSaleDetailLC(generics.ListCreateAPIView):
    queryset = PaymentSaleDetail.objects.all()
    serializer_class = PaymentSaleDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["sale_detail", "payment"]
    permission_classes = [permissions.IsAdminUser | HasModelPermission]
    model_permissions = {
        "GET": ["app.view_paymentsaledetail"],
        "POST": ["app.add_paymentsaledetail"],
    }

    @extend_schema(
        tags=["Payment"],
        operation_id="Listar Detalles de Pagos de Venta",
        description=(
            "Ruta para listar detalles de pagos asociados a ventas. Requiere permiso "
            "`view_paymentsaledetail` o ser administrador."
        ),
        parameters=[
            OpenApiParameter(
                name="sale_detail",
                type=int,
                location=OpenApiParameter.QUERY,
                required=True,
                description="ID del detalle de la venta."
            ),
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
        sale_detail = request.query_params.get("sale_detail")
        if not sale_detail:
            return Response(
                {"sale_detail": ["Este campo es requerido."]},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().get(request, *args, **kwargs)

    @extend_schema(
        tags=["Payment"],
        operation_id="Crear Detalle de Pago de Venta",
        description=(
            "Ruta para crear un detalle de pago asociado a una venta. Requiere permiso "
            "`add_paymentsaledetail` o ser administrador."
        ),
        request=inline_serializer(
            name="PaymentSaleDetailCreate",
            fields={
                "sale_detail": serializers.IntegerField(),
                "payment": serializers.IntegerField(),
                "amount": serializers.DecimalField(max_digits=50, decimal_places=2),
            }
        )
    )
    def post(self, request, *args, **kwargs):
        request.data["created_by"] = request.user.pk
        return super().post(request, *args, **kwargs)
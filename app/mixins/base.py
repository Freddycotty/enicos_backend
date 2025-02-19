from rest_framework.pagination import PageNumberPagination

class OptionalPaginationMixin:
    def paginate_queryset(self, queryset):
        request = self.request
        no_pagination = request.query_params.get('no_pagination')

        if no_pagination and no_pagination.lower() in ['true', '1']:
            return None  # Desactiva la paginación
        
        return super().paginate_queryset(queryset)
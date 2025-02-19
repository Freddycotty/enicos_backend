import django_filters
from app.models.category import Category

class CategoryFilter(django_filters.FilterSet):
    is_main = django_filters.BooleanFilter(method="filter_main_category")

    class Meta:
        model = Category
        fields = ["is_main", 'parent']

    def filter_main_category(self, queryset, name, value):
        print("hola")
        """Si `is_main=true`, devuelve solo categorías principales. Si `false`, devuelve solo subcategorías."""
        if value:
            return queryset.filter(parent__isnull=True)
        return queryset.filter(parent__isnull=False)



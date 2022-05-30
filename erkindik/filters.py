from django_filters import rest_framework as filters
from .models import Art


class ArtFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Art
        fields = ["genre", "year", "status", "min_price", "max_price"]

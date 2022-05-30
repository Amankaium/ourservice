from django_filters import rest_framework as filters
from .models import Flight


class FlightFilter(filters.FilterSet):
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")

    class Meta:
        model = Flight
        fields = ["from_city", "to_city", "aviacompany", "max_price", "min_price"]
from .models import Apartment
from django_filters import rest_framework as filters


class ApartmentsFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Apartment
        fields = ["min_price", "max_price"] + [field.name for field in Apartment._meta.get_fields() if field.name != "photo"]

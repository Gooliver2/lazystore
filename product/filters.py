from django_filters import rest_framework as filters

from product.models import Product


class ProductFilter(filters.FilterSet):
    price_lte = filters.NumberFilter(name="price", lookup_expr='lte')
    price_gte = filters.NumberFilter(name="price", lookup_expr='gte')

    class Meta:
        model = Product
        fields = ['name', 'type',
                  'price_gte', 'price_lte']

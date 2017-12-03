from django_filters import rest_framework as filters

from bucket.models import Bucket


class BucketFilter(filters.FilterSet):
    created_at_gte = filters.DateTimeFilter(name="created_at", lookup_expr='gte')
    created_at_lte = filters.DateTimeFilter(name="created_at", lookup_expr='lte')
    updated_at_gte = filters.DateTimeFilter(name="updated_at", lookup_expr='gte')
    updated_at_lte = filters.DateTimeFilter(name="updated_at", lookup_expr='lte')

    class Meta:
        model = Bucket
        fields = ['status', 'card',
                  'created_at_gte', 'created_at_lte',
                  'updated_at_gte', 'updated_at_lte']

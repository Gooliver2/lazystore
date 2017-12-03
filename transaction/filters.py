from django_filters import rest_framework as filters

from transaction.models import Transaction


class TransactionFilter(filters.FilterSet):
    sum_lte = filters.NumberFilter(name="sum", lookup_expr='lte')
    sum_gte = filters.NumberFilter(name="sum", lookup_expr='gte')
    cash_lte = filters.NumberFilter(name="cash", lookup_expr='lte')
    cash_gte = filters.NumberFilter(name="cash", lookup_expr='gte')
    change_lte = filters.NumberFilter(name="change", lookup_expr='lte')
    change_gte = filters.NumberFilter(name="change", lookup_expr='gte')

    created_at_gte = filters.DateTimeFilter(name="created_at", lookup_expr='gte')
    created_at_lte = filters.DateTimeFilter(name="created_at", lookup_expr='lte')
    updated_at_gte = filters.DateTimeFilter(name="updated_at", lookup_expr='gte')
    updated_at_lte = filters.DateTimeFilter(name="updated_at", lookup_expr='lte')

    class Meta:
        model = Transaction
        fields = ['bucket', 'payment_type',
                  'sum_lte', 'sum_gte',
                  'cash_lte', 'cash_gte',
                  'change_lte', 'change_gte',
                  'created_at_gte', 'created_at_lte',
                  'updated_at_gte', 'updated_at_lte']

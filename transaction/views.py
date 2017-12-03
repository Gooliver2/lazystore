from rest_framework import generics

from transaction.filters import TransactionFilter
from transaction.models import Transaction
from transaction.serializers import TransactionSerializer, TransactionCreateSerializer


class TransactionListView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    filter_class = TransactionFilter
    ordering_fields = ('bucket', 'payment_type', 'sum', 'cash', 'change', 'created_at', 'updated_at')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TransactionCreateSerializer
        return TransactionSerializer


class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

from rest_framework import generics

from transaction.models import Transaction
from transaction.serializers import TransactionCreateSerializer, TransactionListSerializer, TransactionDetailSerializer


class TransactionListView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TransactionCreateSerializer
        return TransactionListSerializer


class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionDetailSerializer

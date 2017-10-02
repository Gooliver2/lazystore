from rest_framework import generics

from card.models import Card
from card.serializers import CardDetailSerializer, CardListSerializer, CardCreateSerializer


class CardListView(generics.ListCreateAPIView):
    queryset = Card.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CardCreateSerializer
        return CardListSerializer


class CardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardDetailSerializer

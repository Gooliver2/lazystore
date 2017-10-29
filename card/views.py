from rest_framework import generics

from card.models import Card
from card.serializers import CardSerializer


class CardListView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

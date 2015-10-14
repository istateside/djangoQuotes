from django.views.generic.base import TemplateView
from .models import Quote, Source, Author
from .serializers import QuoteSerializer, SourceSerializer, AuthorSerializer
from rest_framework import generics

class QuoteList(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
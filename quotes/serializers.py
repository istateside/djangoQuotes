from rest_framework import serializers
from quotes.models import Author, Source, Quote

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('id', 'body', 'source')
        
class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('id', 'title', 'author', 'pub_date')
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name')
        

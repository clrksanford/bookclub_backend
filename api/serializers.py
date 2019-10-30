from rest_framework import serializers
from api.models import Book, Event


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Event
        fields = '__all__'

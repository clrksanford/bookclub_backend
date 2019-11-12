from rest_framework import serializers
from api.models import Book, Event


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=False)
    attendees = serializers.StringRelatedField(many=True)

    def create(self, validated_data):
        book = validated_data.pop('book')
        book = Book.objects.create(**book)
        event = Event.objects.create(**validated_data)
        event.book = book
        event.save()
        return event

    class Meta:
        model = Event
        fields = '__all__'

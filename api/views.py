from django.http import HttpResponse
from django.views import View
from rest_framework.decorators import action
from rest_framework import viewsets
from api.models import Book, Event, User
from api.serializers import BookSerializer, EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-date')
    serializer_class = EventSerializer

    @action(detail=True, methods=['post'])
    def rsvp(self, request, pk=None):
        event = self.get_object()
        username = request.data.get('username', '')
        user = User.objects.filter(username=username).first()
        user.events.add(event)
        user.save()

        return HttpResponse(status=200)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

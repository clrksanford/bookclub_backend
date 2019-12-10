from django.contrib import admin
from api.models import Book, Event, User

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Event)

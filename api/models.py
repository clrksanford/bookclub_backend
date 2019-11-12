from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    cover_url = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    blurb = models.CharField(max_length=500)


class Event(models.Model):
    title = models.CharField(max_length=100)
    book = models.ForeignKey(to=Book, null=True, on_delete=models.SET_NULL)
    date = models.DateField()
    description = models.CharField(max_length=500)


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    events = models.ManyToManyField('Event', related_name='attendees')

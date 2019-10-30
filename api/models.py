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

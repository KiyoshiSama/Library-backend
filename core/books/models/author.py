from django.db import models
from .book import Book


class Author(models.Model):
    name = models.CharField(max_length=225)
    books = models.ManyToManyField(Book)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

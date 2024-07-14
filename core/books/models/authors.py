from django.db import models
from .books import Book


class Author(models.Model):
    name = models.CharField(max_length=225)
    writed_books = models.ManyToManyField('Book', related_name='authors', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"] 

    def __str__(self):
        return self.name


from django.db import models
from accounts.models import User
from .categories import Category
from .publishers import Publisher


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_date = models.DateField()
    page_number = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

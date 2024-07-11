from rest_framework import serializers
from ..models import Author, Book, Category, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "writed_books"]
        extra_kwargs = {"writed_books": {"required": False}}


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        ordering = ["title"]
        model = Book
        fields = (
            "id",
            "title",
            "description",
            "publisher",
            "category",
            "publish_date",
            "page_number",
            "authors",
        )
        extra_kwargs = {"authors": {"required": False}}


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["id", "name", "address"]

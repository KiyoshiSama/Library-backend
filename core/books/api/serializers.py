from rest_framework import serializers
from ..models import Author, Book, Category, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "id",
            "name",
            "writed_books",
        ]


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "category",
            "page_number",
        )


class BookDetailSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
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

    def create(self, validated_data):
        authors_data = validated_data.pop("authors")
        book = Book.objects.create(**validated_data)
        for author_data in authors_data:
            author, created = Author.objects.get_or_create(
                name=author_data["name"], defaults=author_data
            )
            author.writed_books.add(book)
        return book

    def update(self, instance, validated_data):
        authors_data = validated_data.pop("authors")
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.publisher = validated_data.get("publisher", instance.publisher)
        instance.category = validated_data.get("category", instance.category)
        instance.publish_date = validated_data.get(
            "publish_date", instance.publish_date
        )
        instance.page_number = validated_data.get("page_number", instance.page_number)
        instance.save()

        instance.authors.clear()
        for author_data in authors_data:
            author_id = author_data.get("id")
            if author_id:
                author = Author.objects.get(id=author_id)
                author.name = author_data.get("name", author.name)
                author.save()
            else:
                author, created = Author.objects.get_or_create(
                    name=author_data["name"], defaults=author_data
                )
            author.writed_books.add(instance)

        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["id", "name", "address"]

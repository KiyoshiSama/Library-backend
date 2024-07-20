from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from books.api.serializers import (
    AuthorSerializer,
    BookCreateUpdateSerializer,
    BookRetrieveSerializer,
    CategorySerializer,
    PublisherSerializer,
)
from books.models import Author, Book, Publisher, Category


class AuthorsViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()


class BooksViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [
        "is_available",
    ]
    search_fields = [
        "name",
    ]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BookRetrieveSerializer
        return BookCreateUpdateSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class PublishersViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()

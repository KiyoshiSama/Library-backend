from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import (
    AuthorSerializer,
    BookCreateUpdateSerializer,
    BookRetrieveSerializer,
    CategorySerializer,
    PublisherSerializer,
)
from ..models import Author, Book, Publisher, Category
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


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

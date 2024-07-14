from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import (
    AuthorSerializer,
    BookDetailSerializer,
    BookListSerializer,
    CategorySerializer,
    PublisherSerializer,
)
from ..models import Author, Book, Publisher, Category
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class AuthorsViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()



class BooksViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    def get_serializer_class(self):
        if self.action == "list":
            return BookListSerializer
        return BookDetailSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class PublishersViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()

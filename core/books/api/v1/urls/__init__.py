from django.urls import path, include

urlpatterns = [
    path("", include("books.api.v1.urls.books_urls")),
]

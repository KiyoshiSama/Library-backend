from django.urls import path, include
from .routers import router as books_router

app_name = "books-api"

urlpatterns = [
    path('', include("books.api.routers")),
]

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import renderers

app_name= "books-api"

router = DefaultRouter()
router.register(r'authors', views.AuthorsViewSet, basename='authors')
router.register(r'books', views.BooksViewSet, basename='books')
router.register(r'categories', views.CategoriesViewSet, basename='categories')
router.register(r'publishers', views.PublishersViewSet, basename='publishers')

urlpatterns = [
    path('', include(router.urls)),
]

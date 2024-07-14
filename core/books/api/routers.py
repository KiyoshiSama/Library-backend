from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'authors', views.AuthorsViewSet, basename='authors')
router.register(r'books', views.BooksViewSet, basename='books')
router.register(r'categories', views.CategoriesViewSet, basename='categories')
router.register(r'publishers', views.PublishersViewSet, basename='publishers')

urlpatterns = [
    path("", include(router.urls)),

]

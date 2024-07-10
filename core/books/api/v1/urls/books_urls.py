from django.urls import path, include
from .. import views
from rest_framework.routers import DefaultRouter
from rest_framework import renderers

router = DefaultRouter()
router.register(r'authors', views.AuthorsViewSet, basename='authors')
router.register(r'books', views.BooksViewSet, basename='books')
router.register(r'categories', views.CategoriesViewSet, basename='categories')
router.register(r'publishers', views.PublishersViewSet, basename='publishers')

urlpatterns = [
    path('', include(router.urls)),
]
# authors_list = views.AuthorsViewSet.as_view({
#     'get': 'list',
#     'post':'create'
# })
# authors_detail = views.AuthorsViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# books_list = views.AuthorsViewSet.as_view({
#     'get': 'list',
#     'post':'create'
# })
# books_detail = views.AuthorsViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# categories_list = views.AuthorsViewSet.as_view({
#     'get': 'list',
#     'post':'create'
# })
# categories_detail = views.AuthorsViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# publishers_list = views.AuthorsViewSet.as_view({
#     'get': 'list',
#     'post':'create'
# })
# publishers_detail = views.AuthorsViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

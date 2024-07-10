from django.urls import path, include
from .. import views

urlpatterns = [
    path("",views.UserViewSet.as_view(),name="user-view")
]
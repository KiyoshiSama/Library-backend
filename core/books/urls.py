from django.urls import include, path

app_name = "books"


urlpatterns = [

    path("api/v1/", include("books.api.v1.urls")),
]
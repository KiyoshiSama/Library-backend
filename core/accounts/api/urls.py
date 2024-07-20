from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.api import views

app_name = "accounts-api"

urlpatterns = [
    path("", views.UserProfileGenericView.as_view(), name="accounts"),
    path("token-create/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token-refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("create-account/", views.RegisterUserAPIView.as_view(), name="create-account"),
    path(
        "active-account/",
        views.ActiveAccountGenericApiView.as_view(),
        name="active-account",
    ),
]

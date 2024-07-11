from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from rest_framework import renderers

app_name = "accounts-api"

router = DefaultRouter()
router.register(
    r"account-details", views.UserProfileViewSet, basename="account-details"
)
urlpatterns = [
    path("token-create/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token-refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("", include(router.urls)),
    path("create-account/", views.RegisterUserAPIView.as_view(), name="create-account"),
]

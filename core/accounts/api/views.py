import random
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status, generics
from mail_templated import EmailMessage
from accounts.api.serializers import (
    UserProfileSerializer,
    UserRegisterSerializer,
    VerificationCodeSerialzier,
)
from accounts.models.users import User


class RegisterUserAPIView(generics.GenericAPIView):

    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        verification_code = str(random.randint(10000, 99999))
        user.verification_code = verification_code
        user.save()
        email = serializer.validated_data["email"]
        email_obj = EmailMessage(
            "email/activation_email.tpl",
            {"verification_code": verification_code},
            "admin@admin.com",
            to=[email],
        )
        email_obj.send()

        data = {"User email": user.email}
        return Response(data, status=status.HTTP_201_CREATED)


class ActiveAccountGenericApiView(generics.GenericAPIView):
    serializer_class = VerificationCodeSerialzier
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"detail": "Account confirmed successfully"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileGenericView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, email=self.request.user.email)

        return obj

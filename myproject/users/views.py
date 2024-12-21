# myproject/users/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserRegistrationSerializer, UserSerializer
from .services import UserService
from .permissions import IsAuthenticatedAndActive

class UserRegisterView(generics.CreateAPIView):
    """
    Endpoint for user registration.
    """
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user_service = UserService()
        user_service.register_user(email, password)

class CurrentUserView(generics.RetrieveAPIView):
    """
    Endpoint to get the current logged-in user's data.
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedAndActive]

    def get_object(self):
        return self.request.user


# JWT endpoints provided by simplejwt:
# /token/ (POST): obtain token
# /token/refresh/ (POST): refresh token

class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]

class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]

from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from auth_user.serializers import RegistrationsUserSerializer


@extend_schema(tags=['Auth'], summary='Authenticate user')
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema(tags=['Auth'], summary='Refresh token')
class CustomTokenRefreshView(TokenRefreshView):
    pass


@extend_schema(tags=['Auth'], summary='Registrations', responses={200: RegistrationsUserSerializer})
class RegisterUserView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationsUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

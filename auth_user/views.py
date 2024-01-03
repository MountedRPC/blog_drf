from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, generics
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from auth_user.serializers import RegistrationsUserSerializer


@extend_schema(tags=['Auth'], summary='Authenticate user')
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema(tags=['Auth'], summary='Refresh token')
class CustomTokenRefreshView(TokenRefreshView):
    pass


@extend_schema(tags=['Auth'], summary='Registrations')
class RegisterUserView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationsUserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

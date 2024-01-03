from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import permissions, viewsets

from accounts.serializers import UserSerializer


@extend_schema(tags=['Accounts'])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

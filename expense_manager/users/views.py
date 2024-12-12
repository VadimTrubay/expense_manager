from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

from users.serializers import CustomUserSerializer


class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

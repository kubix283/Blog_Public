from rest_framework.response import Response
from .serializers import UserSerializer
from accounts.models import CustomUser
from rest_framework import generics


class ListUsersAPI(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    







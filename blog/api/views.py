from rest_framework.response import Response
from .serializers import UserSerializer, UserUpdateSerializer
from accounts.models import CustomUser
from rest_framework import generics, permissions, status



class ListUsersAPI(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class RetrieveUpdateDestroyUsersAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAdminUser]





    







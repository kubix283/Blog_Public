from .serializers import UserSerializer, UserUpdateSerializer, PostSerializer
from accounts.models import CustomUser
from blog_app.models import Post, Comment
from .permissions import IsOwnerOrReadOnly, IsOwnerAndAdmin
from rest_framework import generics, permissions


class ListUsersAPI(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class RetrieveUpdateDestroyUsersAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAdminUser]


class ListPostAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class RetrieveUpdatePostAPI(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class DestroyPostAPI(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerAndAdmin, permissions.IsAuthenticated]










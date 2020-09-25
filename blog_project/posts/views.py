from django.contrib.auth import get_user_model
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthOrReadOnly


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

from django.contrib.auth import get_user_model
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAdminUser

from articles.models import Article
from .serializers import UserSerializer, ArticleSerializer
from .permissions import IsAuthorOrReadOnly

User = get_user_model()


class SignUp(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleRead(ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Author').exists():
            return Article.objects.all()
        if user.groups.filter(name='Follower').exists():
            return Article.objects.filter(public=False)
        return Article.objects.filter(public=True)


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Author').exists():
            return Article.objects.all()
        if user.groups.filter(name='Follower').exists():
            return Article.objects.filter(public=False)
        return Article.objects.filter(public=True)


class ArticleCreate(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
        )

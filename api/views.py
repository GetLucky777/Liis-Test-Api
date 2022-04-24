from django.contrib.auth import get_user_model
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from articles.models import Article

from .permissions import IsAuthorOrReadOnly, IsAuthorUser
from .serializers import ArticleSerializer, UserSerializer

User = get_user_model()


class SignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleReadView(ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Author').exists():
            return Article.objects.all()
        if user.groups.filter(name='Follower').exists():
            return Article.objects.filter(public=False)
        return Article.objects.filter(public=True)


class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Author').exists():
            return Article.objects.all()
        if user.groups.filter(name='Follower').exists():
            return Article.objects.filter(public=False)
        return Article.objects.filter(public=True)


class ArticleCreateView(CreateAPIView):
    permission_classes = [IsAuthorUser]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
        )

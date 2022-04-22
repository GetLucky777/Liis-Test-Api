from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

from articles.models import Article
from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

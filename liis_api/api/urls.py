from django.urls import path

from .views import UserViewSet

urlpatterns = [
    path('create_user/', UserViewSet.as_view()),
]

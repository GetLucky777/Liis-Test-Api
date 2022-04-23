from django.urls import path

from .views import (
    SignUp,
    ArticleCreate,
    ArticleRead,
    ArticleDetail
)


urlpatterns = [
    path('signup/', SignUp.as_view()),
    path('create_article/', ArticleCreate.as_view()),
    path('articles/', ArticleRead.as_view()),
    path('articles/<int:pk>/', ArticleDetail.as_view()),
]

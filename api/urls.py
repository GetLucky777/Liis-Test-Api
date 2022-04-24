from django.urls import path

from .views import (ArticleCreateView, ArticleDetailView,
                    ArticleReadView, SignUpView)

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('create_article/', ArticleCreateView.as_view()),
    path('articles/', ArticleReadView.as_view()),
    path('articles/<int:pk>/', ArticleDetailView.as_view()),
]

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Article(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Заголовок статьи'
    )
    text = models.TextField(
        verbose_name='Текст статьи'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='articles',
        verbose_name='Автор статьи'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации статьи'
    )

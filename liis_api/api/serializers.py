from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from django.forms import ValidationError
from rest_framework import serializers

from liis_api.articles.models import Article

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='username')

    class Meta:
        model = User
        fields = (
            'email',
            'password',
        )

    def validate(self, data):
        validate_password(data['password'])
        validate_email(data['username'])
        if User.objects.filter(username=data['username']).exists():
            raise ValidationError(
                'Пользователь с таким email уже существует!'
            )
        return data

    def create(self, validated_data):
        new_user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        follower_group = Group.objects.get(
            name='Follower'
        )
        follower_group.user_set.add(new_user)
        return new_user


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Article
        fields = (
            'title',
            'text',
            'public',
            'author'
        )
        read_only_fields = ('author', )

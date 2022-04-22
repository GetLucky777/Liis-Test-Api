from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    login = serializers.CharField(source='username')

    class Meta:
        model = User
        fields = (
            'login',
            'password',
        )
    
    def validate(self, data):
        validate_password(data['password'])
        validate_email(data['username'])
        return data

    def create(self, validated_data):
        new_user = User.objects.create(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        follower_group = Group.objects.get(
            name='Follower'
        )
        follower_group.user_set.add(new_user)
        return new_user

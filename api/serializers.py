from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Post, Comment
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password' )
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            validated_data['password'] = make_password(validated_data['password'])
            user = User.objects.create(validated_data['first_name'], validated_data['last_name'], validated_data['username'], validated_data['email'], 
            validated_data['password'])
            return user
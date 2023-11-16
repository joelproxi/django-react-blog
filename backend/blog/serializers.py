from rest_framework import serializers
from accounts.serializers import UserSerializer

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'author',
            'created',
            'updated',
        )
        extra_kwargs = {
            'author': {'read_only': True},
        }


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'id',
            'content',
            'author',
            'created',
            'updated',
        )
        extra_kwargs = {
            'author': {'read_only': True},
        }

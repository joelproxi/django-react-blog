# from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from blog.models import Comment, Post
from blog.serializers import PostSerializer, CommentSerializer


class PostViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(status='P')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

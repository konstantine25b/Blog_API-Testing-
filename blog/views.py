from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Post, Comment, Tag
from .serializers import PostSerializer , CommentSerializer , TagSerializer


class PostList(generics.ListCreateAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer
    


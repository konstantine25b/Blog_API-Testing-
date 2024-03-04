from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PostList.as_view() , name = 'post-list'),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('posts/', CommentList.as_view() , name = 'comment-list'),
    path('comment/<int:pk>', CommentDetail.as_view()),
    path('tags/', TagList.as_view() , name = 'tag-list'),
    path('tag/<int:pk>', TagDetail.as_view()),
]

from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import *
from rest_framework.viewsets import GenericViewSet

from .serializer import *
from .ViewSet import *


from rest_framework.pagination import PageNumberPagination


class PostPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CommentPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 10000


class PostList(generics.ListAPIView):
    serializer_class = PostsSerializer
    pagination_class = PostPagination

    def get_queryset(self):
        book_id = self.kwargs["pk"]
        return Posts.objects.filter(book_id=book_id)


class PostCreate(generics.CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentList(generics.ListAPIView):
    serializer_class = CommentsSerializer
    pagination_class = CommentPagination

    def get_queryset(self):
        post_id = self.kwargs["pk"]
        return Comment.objects.filter(post_id=post_id)


class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]






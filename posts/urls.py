from rest_framework import routers
from django.urls import path, include

from .views import *


router = routers.SimpleRouter()

# router.register(r'posts', PostsViewSet, basename='PostsViewSet')
# router.register(r'comments', CommentsViewSet, basename='CommentsViewSet')

urlpatterns = [
    path('posts/<int:pk>/', PostList.as_view()),
    path('posts/', PostCreate.as_view()),
    path('comments/<int:pk>/', CommentList.as_view()),
    path('comments/', CommentCreate.as_view()),
    # path('', include(router.urls))
]

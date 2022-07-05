from rest_framework import serializers
from .models import *


class PostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = "__all__"


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"



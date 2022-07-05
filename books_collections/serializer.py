from rest_framework import serializers
from .models import *


class TypeBookmarksSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TypeBookmarks
        fields = "__all__"


class BookmarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmarks
        fields = "__all__"



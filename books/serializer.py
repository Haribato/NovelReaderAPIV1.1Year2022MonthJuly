from rest_framework import serializers
from .models import *


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"


class AuthorListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name


class CategoryListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name


class BooksSerializer(serializers.ModelSerializer):

    authors = AuthorListingField(many=True, read_only=True)
    categories = CategoryListingField(many=True, read_only=True)
    img = serializers.ImageField(required=False)

    class Meta:
        model = Books
        fields = "__all__"
        owner = serializers.Field(source=settings.MEDIA_URL)


class ChaptersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapters
        fields = '__all__'


class LikeListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.id


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'










from django.shortcuts import render
from requests import Response
from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import *
from rest_framework.parsers import MultiPartParser, FormParser

from .models import *
from .pagination import BooksPagination
from .serializer import *
from .permissions import *


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAdminOrReadOnly]


class StatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = [IsAdminOrReadOnly]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]


class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = BooksPagination
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        return Books.objects.all()


class RatingsViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Ratings.objects.all()

# def img(request, sl):
#
#     return Response({'img': upload})







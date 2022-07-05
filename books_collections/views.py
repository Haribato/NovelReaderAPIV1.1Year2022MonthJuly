from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import *
from .serializer import *


class TypeBookmarksViewSet(viewsets.ModelViewSet):
    queryset = TypeBookmarks.objects.all()
    serializer_class = TypeBookmarksSerializer
    permission_classes = [IsAuthenticated]


class BookmarksViewSet(viewsets.ModelViewSet):
    queryset = Bookmarks.objects.all()
    serializer_class = BookmarksSerializer
    permission_classes = [IsAuthenticated]



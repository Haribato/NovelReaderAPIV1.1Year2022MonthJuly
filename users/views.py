from django.shortcuts import render
from rest_framework.permissions import AllowAny

from .models import CustomUser
from .serializer import *
from rest_framework import generics


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

from django.shortcuts import render

# Create your views here.
# call/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import VideoCall
from .serializers import VideoCallSerializer

class VideoCallViewSet(viewsets.ModelViewSet):
    queryset = VideoCall.objects.all()
    serializer_class = VideoCallSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
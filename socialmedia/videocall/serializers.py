# call/serializers.py

from rest_framework import serializers
from .models import VideoCall

class VideoCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCall
        fields = ['id', 'sender', 'receiver', 'room_name', 'created_at']
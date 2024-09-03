from rest_framework import serializers
from .models import Chat, Message

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'timestamp']

class ChatSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    user1 = serializers.StringRelatedField(read_only=True)
    user2 = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'user1', 'user2', 'created_at', 'messages']

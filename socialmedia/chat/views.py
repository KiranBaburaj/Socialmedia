from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from accounts import serializers
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user1 = request.user
        user2_id = request.data.get('user2')
        if not user2_id:
            return Response({"error": "User2 is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user2 = User.objects.get(id=user2_id)
        except User.DoesNotExist:
            return Response({"error": "User2 does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        if user1 == user2:
            return Response({"error": "Cannot create a chat with yourself."}, status=status.HTTP_400_BAD_REQUEST)

        chat, created = Chat.objects.get_or_create(user1=user1, user2=user2)
        if not created:
            chat, created = Chat.objects.get_or_create(user1=user2, user2=user1)
        
        serializer = self.get_serializer(chat)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        chat_id = self.request.data.get('chat')
        try:
            chat = Chat.objects.get(id=chat_id)
        except Chat.DoesNotExist:
            raise serializers.ValidationError({"error": "Chat does not exist."})
        
        if self.request.user not in [chat.user1, chat.user2]:
            raise serializers.ValidationError({"error": "You are not a participant in this chat."})
        
        serializer.save(sender=self.request.user, chat=chat)

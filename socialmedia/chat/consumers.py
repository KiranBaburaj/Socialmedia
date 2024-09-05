import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from django.apps import apps
from django.db.models import Q

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        print(f"User {self.user} connecting to room {self.room_group_name}")

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        print(f"User {self.user} accepted in room {self.room_group_name}")

    async def disconnect(self, close_code):
        print(f"User {self.user} disconnecting from room {self.room_group_name}")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        sender_id = data['sender_id']
        receiver_id = data['receiver_id']

        try:
            sender = await self.get_user(sender_id)
            receiver = await self.get_user(receiver_id)
            chat = await self.get_chat(self.room_name, sender, receiver)
            new_message = await self.create_message(chat, sender, receiver, message)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': new_message.content,
                    'sender': new_message.sender.username,
                    'receiver': new_message.receiver.username,
                    'timestamp': str(new_message.timestamp),
                }
            )
        except Exception as e:
            print(f"Error receiving message: {str(e)}")  # Log error
            await self.send(text_data=json.dumps({
                'error': str(e)
            }))

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        receiver = event['receiver']
        timestamp = event['timestamp']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'receiver': receiver,
            'timestamp': timestamp,
        }))

    @database_sync_to_async
    def get_user(self, user_id):
        User = get_user_model()
        return User.objects.get(id=user_id)

    @database_sync_to_async
    def get_chat(self, room_name, sender, receiver):
        Chat = apps.get_model('chat', 'Chat')
        try:
            return Chat.objects.get(
                Q(user1=sender, user2=receiver) | Q(user1=receiver, user2=sender)
            )
        except Chat.DoesNotExist:
            new_chat = Chat.objects.create(user1=sender, user2=receiver)
            return new_chat

    @database_sync_to_async
    def create_message(self, chat, sender, receiver, content):
        Message = apps.get_model('chat', 'Message')
        return Message.objects.create(chat=chat, sender=sender, receiver=receiver, content=content)
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Chat, Message
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Add user to the chat group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Remove user from the chat group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        user_id = data['user_id']

        try:
            user = User.objects.get(id=user_id)
            chat = Chat.objects.get(id=self.room_name)  # Assuming room_name is chat ID
            new_message = Message.objects.create(chat=chat, sender=user, content=message)
            new_message.save()

            # Broadcast the message to the group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': new_message.content,
                    'user': new_message.sender.username,
                    'timestamp': str(new_message.timestamp),
                }
            )
        except Chat.DoesNotExist:
            await self.send(text_data=json.dumps({
                'error': 'Chat room does not exist.'
            }))

    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        timestamp = event['timestamp']

        # Send the message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
            'timestamp': timestamp,
        }))

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class VideoCallConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'video_call_{self.room_name}'

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json['type']
        message_data = text_data_json['data']

        # Use a consistent naming convention for the channel layer
        channel_message_type = f'send_{message_type.replace("-", "_")}'

        await self.channel_layer.group_send(self.room_group_name, {
            'type': channel_message_type,
            'data': message_data
        })

    async def send_ready(self, event):
        await self.send(text_data=json.dumps({
            'type': 'ready',
            'data': event['data']
        }))

    async def send_offer(self, event):
        await self.send(text_data=json.dumps({
            'type': 'offer',
            'data': event['data']
        }))

    async def send_answer(self, event):
        await self.send(text_data=json.dumps({
            'type': 'answer',
            'data': event['data']
        }))

    async def send_ice_candidate(self, event):
        await self.send(text_data=json.dumps({
            'type': 'ice-candidate',
            'data': event['data']
        }))
# socialmedia/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.room_group_name = f"notifications_{self.user_id}"

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data['type'] == 'incoming-call':
            # Forward the incoming call notification to the appropriate user
            await self.channel_layer.group_send(
                f"notifications_{data['data']['to']}",
                {
                    'type': 'send_notification',
                    'message': data
                }
            )

    async def send_notification(self, event):
        # Send a message to WebSocket
        await self.send(text_data=json.dumps(event["message"]))
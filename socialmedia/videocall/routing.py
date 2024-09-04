# videocall/routing.py

from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    
re_path(r'ws/video_call/(?P<room_name>[\w-]+)/$', consumers.VideoCallConsumer.as_asgi()),
       re_path(r"ws/notifications/(?P<user_id>\d+)/$", consumers.NotificationConsumer.as_asgi()),
]


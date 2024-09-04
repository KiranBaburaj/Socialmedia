from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatViewSet, MessageViewSet,ChatMessageViewSet

router = DefaultRouter()
router.register(r'chats', ChatViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('<int:chat_id>/messages/', ChatMessageViewSet.as_view({'get': 'list'}), name='chat-messages-list'),

]

from django.db import models

# Create your models here.
# call/models.py

from django.db import models
from django.contrib.auth.models import User

class VideoCall(models.Model):
    sender = models.ForeignKey(User, related_name='sent_calls', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_calls', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    room_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Call from {self.sender.username} to {self.receiver.username} in {self.room_name}"
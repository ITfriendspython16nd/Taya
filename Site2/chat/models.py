from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ChatRoom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE,related_name='messages')
    text = models.TextField()

    def __str__(self):
        return self.name
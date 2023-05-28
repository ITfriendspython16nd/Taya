from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
     title = models.CharField(max_length=255)
     text = models.TextField()
     author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
     image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)
     category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
     
     def get_absolute_url(self):
          return reverse('home')

     def __str__(self):
          return self.title

class Category(models.Model):
     name = models.CharField(max_length=255)

     def __str__(self):
          return self.name
     

class ChatRoom(models.Model):
     name = models.CharField(max_length=60)

     def __str__(self):
          return self.name


class Message(models.Model):
     author = models.ForeignKey(User, on_delete=models.PROTECT, default="Anonim")
     text = models.TextField()
     room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')


from django.shortcuts import render
from chat.models import *

# Create your views here.
def chat_room(request, room_id):
    room = ChatRoom.objects.get(id=room_id)
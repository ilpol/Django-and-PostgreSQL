from django.shortcuts import render
from django.http import HttpResponse

from chats.models import Chat
from django.utils import timezone
import json
from django.template import loader


def add_chat(request, messages, chat_name, users):
	if request.method == 'GET':
	    new_chat = Chat(chat_name=chat_name, messages = messages, users = users)
	    new_chat.save()

	    return HttpResponse("added chat %s with users %s and messages %s" % (chat_name, users, messages))

	    #return HttpResponse("added chat ")


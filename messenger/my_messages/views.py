from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from my_messages.models import Message
from django.utils import timezone
import json
from django.template import loader



def add_message(request, message_text, chat_name, user):
	if request.method == 'GET':
	    new_message = Message(chat_name=chat_name, message_text = message_text, user = user)
	    new_message.save()

	    return HttpResponse("added message %s to chat %s from user %s" % (message_text, chat_name, user))

	    #return HttpResponse("added message")

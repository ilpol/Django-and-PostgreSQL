import datetime
from django.db import models
from django.utils import timezone
from users.models import User

class Message(models.Model):
    message_text = models.CharField(max_length=200, default='')
    user = models.CharField(max_length=200, default='')
    chat_name = models.CharField(max_length=200, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

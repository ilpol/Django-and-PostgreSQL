import datetime
from django.db import models
from django.utils import timezone


class Chat(models.Model):
    chat_name = models.CharField(max_length=200, default='')
    users = models.CharField(max_length=200, default='')
    messages = models.CharField(max_length=200, default='')

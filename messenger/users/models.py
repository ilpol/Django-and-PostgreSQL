import datetime
from django.db import models
from django.utils import timezone
from chats.models import Chat

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200, default='')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, default="")
    hobby = models.CharField(max_length=200, default='')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


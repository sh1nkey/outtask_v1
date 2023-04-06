import datetime
import uuid

from django.db import models

# Create your models here.
from users.models import User


class Room(models.Model):
    name = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
class Messages(models.Model):
    value = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    is_verified_email = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)





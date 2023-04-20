from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Uni(models.Model):
    uni_name = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f'{self.uni_name}'


class User(AbstractUser):
    is_verified_email = models.BooleanField(default=False)
    uni = models.ForeignKey(Uni, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField(default=0)
    socnet_link = models.URLField(blank=True, null=True)





from django.db import models
from users.models import User

# Create your models here.


class Subject(models.Model):
    subj_name = models.CharField(blank=True, max_length=30)

    def __str__(self):
        return f'{self.subj_name}'

class Uni(models.Model):
    uni_name = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f'{self.uni_name}'



class Offer(models.Model):
    subj = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
    uni = models.ForeignKey(to=Uni, on_delete=models.CASCADE)
    user= models.ForeignKey(to=User, on_delete=models.CASCADE)
    task = models.CharField(max_length=40)
    price = models.PositiveIntegerField(default=0)
    offer_or_order = models.BooleanField()

    def __str__(self):
        return f'{self.user.username}'


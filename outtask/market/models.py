import django
from django.db import models
from users.models import User
from django.utils.timezone import now
# Create your models here.


class Subject(models.Model):
    subj_name = models.CharField(blank=True, max_length=30)

    def __str__(self):
        return f'{self.subj_name}'

    class Meta:
        ordering = ['subj_name']


'''
Offer =  an thing that a person (customer) leaves on the market to be fulfilled 
'''
class Offer(models.Model):
    subj = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=40)
    price = models.PositiveIntegerField(default=0)
    deadline = models.DateField(blank=True, null=True)
    date_create = models.DateTimeField(default=django.utils.timezone.now)

    class Meta:
        ordering = ['deadline']


'''
Order = suggestions from the worker to work on customer's thing
'''

class Order(models.Model):
    NOT_TAKEN = 0
    TAKEN = 1
    READY = 2

    STATUSES = [
    (NOT_TAKEN, 'Исполнитель ещё не подтвердил, что  будет исполнять ваш заказ'),
    (TAKEN, 'Ваш заказ выполняется'),
    (READY, 'Заказ готов'),
    ]

    offer = models.ForeignKey(to=Offer, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.SmallIntegerField(default=NOT_TAKEN, choices=STATUSES)
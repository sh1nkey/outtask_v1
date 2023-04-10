from django.db import models
from users.models import User
from django.utils.timezone import now
# Create your models here.


class Subject(models.Model):
    subj_name = models.CharField(blank=True, max_length=30)

    def __str__(self):
        return f'{self.subj_name}'

class Offer(models.Model):
    subj = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=40)
    price = models.PositiveIntegerField(default=0)
    deadline = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['deadline']

    def __str__(self):
        return f'{self.user.username}'



# class Order(models.Model):
#     NOT_TAKEN = 0
#     TAKEN = 1
#     READY = 2
#
#     STATUSES = [
#     (NOT_TAKEN, 'Исполнитель ещё не подтвердил, что  будет исполнять ваш заказ'),
#     (TAKEN, 'Ваш заказ выполняется'),
#     (READY, 'Заказ готов'),
#     ]
#
#     offer = models.ForeignKey(to=Offer, on_delete=models.CASCADE)
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE)
#     created_timestamp = models.DateTimeField(auto_now_add=True)
#     status = models.SmallIntegerField(default=NOT_TAKEN, choices=STATUSES)
#     deadline = models.DateField()
from django.db import models
from users.models import User

# Create your models here.


class ModelSubject (models.Model):
    subj_name = models.CharField(blank=True, max_length=30)

    def __str__(self):
        return f'{self.subj_name}'

class ModelUni (models.Model):
    uni_name = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f'{self.uni_name}'



class ModelOfferOrder (models.Model):
    subj_id = models.ForeignKey(to=ModelSubject, on_delete=models.CASCADE)
    uni_id = models.ForeignKey(to=ModelUni, on_delete=models.CASCADE)
    us_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    task = models.CharField(max_length=40)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.us_id}'

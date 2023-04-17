from django import forms


from market.models import Subject
from users.models import Uni, User


class UniForm(forms.Form):
    uni_name = forms.ModelChoiceField(queryset=Uni.objects.all(), label="Фильтрация во ВУЗу:")

    class Meta:
        model = User
        fields = ('uni_name',)


class OfferCreation(forms.Form):
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), label="Предмет:")
    task = forms.CharField(max_length=40, label="Задание кратко:")
    price = forms.IntegerField(label="Цена:")
    deadline = forms.DateField(label="Дедлайн:")

    def __init__(self, *args, **kwargs):
        super(OfferCreation, self).__init__(*args, **kwargs)
        self.label = 'Создать новый заказ:'







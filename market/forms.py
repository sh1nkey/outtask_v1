from django import forms

from market.models import Subject
from users.models import Uni

class UniForm(forms.Form):
    uni_name = forms.ModelChoiceField(queryset=Uni.objects.all())

class OfferCreation(forms.Form):
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())
    task = forms.CharField(max_length=40)
    price = forms.IntegerField()
    deadline = forms.DateField()

from django import forms
from django.contrib.auth.forms import UserChangeForm

from market.models import Subject
from users.models import Uni, User


class UniForm(forms.Form):
    uni_name = forms.ModelChoiceField(queryset=Uni.objects.all())

class OfferCreation(forms.Form):
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())
    task = forms.CharField(max_length=40)
    price = forms.IntegerField()
    deadline = forms.DateField()

class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))


    class Meta:
        model = User
        fields = ('username', )
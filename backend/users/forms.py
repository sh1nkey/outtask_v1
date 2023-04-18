from allauth.account.forms import LoginForm
from django.contrib.auth.forms import UserChangeForm
from django import forms
from users.models import User, Uni


class UniUpdateForm(forms.ModelForm):
    uni_name = forms.ModelChoiceField(queryset=Uni.objects.all())

    class Meta:
        model = User
        fields = ('uni',)


class LoginChangeForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = User
        fields = ('username', )



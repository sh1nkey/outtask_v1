from django import forms

from market.models import Subject
from users.models import Uni

class UniForm(forms.Form):
    uni_name = forms.ModelChoiceField(queryset=Uni.objects.all())


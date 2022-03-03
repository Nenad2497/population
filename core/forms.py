

from django import forms
from .models import Country_data


class ConDataForm(forms.ModelForm):
    class Meta:
        model = Country_data
        fields  = ['country', 'population']
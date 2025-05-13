from django import forms
from django.forms import ModelForm
from smartphone.models import Smartphone

class SmartphoneForm(ModelForm):
    class Meta:
        model = Smartphone
        fields = ['manufacturers','name','ram','storage','screen_size','release_date']


class CompanyForm(forms.Form):
    companies = forms.IntegerField()
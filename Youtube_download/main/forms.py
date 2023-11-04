from django import forms
from django.forms import ModelForm, TextInput

class LinkForm(forms.Form):
    link = forms.CharField(label='Ссылка', max_length=250)
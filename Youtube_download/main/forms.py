
from django.forms import ModelForm, TextInput
from .models import Link
class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['link']

        widgets = {
            "link": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка'
         }),
        }
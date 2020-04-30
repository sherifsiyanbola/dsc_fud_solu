from django import forms
from lga.models import Lga

class LgaForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Name'
        }
    ))
    class Meta:
        model = Lga
        fields = '__all__'
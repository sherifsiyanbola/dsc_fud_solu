from django import forms
from mda.models import Ministry

class MinistryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Name'
        }
    ))
    class Meta:
        model = Ministry
        fields = '__all__'
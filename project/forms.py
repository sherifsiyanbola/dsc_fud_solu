from django import forms
from django.db import transaction
from project.models import Project, Comment, Report, Year
from lga.models import Lga
from mda.models import Ministry
from lga.models import Lga


class YearForm(forms.ModelForm):

    year = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Budget Year'
        }
    ))

    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))

    date_open = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'yyyy-mm-dd'
        }
    ))

    date_closed = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'yyyy-mm-dd'
        }
    ))

    class Meta:
        model = Year
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Title your need'
        }
    ))

    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))

    lga = forms.ModelChoiceField(queryset=Lga.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

    ministry = forms.ModelChoiceField(queryset=Ministry.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

  

    class Meta:
        model = Project
        fields = ('title', 'description', 'lga',
                  'ministry')


class FilterForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    lga = forms.ModelChoiceField(queryset=Lga.objects.all(), required=False, widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

    ministry = forms.ModelChoiceField(queryset=Ministry.objects.all(), required=False, widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

    date = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = Project
        fields = ('title', 'lga', 'ministry', 'date')


class PmpProjectEditForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Title your need'
        }
    ))

    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))

    lga = forms.ModelChoiceField(queryset=Lga.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

    ministry = forms.ModelChoiceField(queryset=Ministry.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

    submittedBy = forms.CharField(label="Full Name", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name'
        }
    ))

    progress_comment = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))

    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'enter your phone number'
        }
    ))

    class Meta:
        model = Project
        exclude = ('date', 'budget_year')


class ProjectFilterForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('date',)


class MinistryProjectEditForm(forms.ModelForm):
    progress_comment = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Project
        fields = ['progress', 'progress_comment']


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Comment'
        }
    ))

    picture = forms.ImageField()

    class Meta:
        model = Comment
        fields = ['text', 'picture']

    def post_comment(self):
        text = self.cleaned_data.get('text')
        picture = self.cleaned_data.get('picture')


class CommentEditForm(forms.ModelForm):

    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Comment'
        }
    ))

    picture = forms.ImageField()

    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'enter your phone number'
        }
    ))

    class Meta:
        model = Comment
        fields = ['text', 'picture', 'phone', 'status']


# report form

class ReportForm(forms.ModelForm):
    report_title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Title your report'
        }
    ))

    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Comment'
        }
    ))

    lga = forms.ModelChoiceField(queryset=Lga.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

    ministry = forms.ModelChoiceField(queryset=Ministry.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

    picture = forms.ImageField()


    class Meta:
        model = Report
        fields = ['report_title', 'text', 'lga', 'ministry',
                  'picture']


class ReportEditForm(forms.ModelForm):

    report_title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter report Title'
        }
    ))

    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Comment'
        }
    ))

    lga = forms.ModelChoiceField(queryset=Lga.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

    ministry = forms.ModelChoiceField(queryset=Ministry.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

    picture = forms.ImageField()

    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'enter your phone number'
        }
    ))

    class Meta:
        model = Report
        fields = ['report_title', 'text', 'lga', 'ministry',
                  'picture', 'phone', 'status']

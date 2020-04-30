from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from mda.models import Ministry
from users.models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model
User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone')


# MINISTRY USER FORM
class MinistryUserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        }
    ))

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }
    ))

    ministry = forms.ModelChoiceField(queryset=Ministry.objects.all(), required=True, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password'
        }
    ))

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'username', 'gender', 'ministry', 'password']

    @transaction.atomic
    def save(self):
        password = self.cleaned_data.pop('password')
        u = super().save()
        u.is_ministryuser = True
        u.set_password(password)
        u.save()
        return u


# GOVERNOR FORM
class GovernorForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        }
    ))

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }
    ))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password'
        }
    ))

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'username', 'gender', 'password']

    @transaction.atomic
    def save(self):
        password = self.cleaned_data.pop('password')
        u = super().save()
        u.is_governor = True
        u.set_password(password)
        u.save()
        return u


# Budget & econ FORM
class BudgetForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        }
    ))

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }
    ))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password'
        }
    ))

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'username', 'gender', 'password']

    @transaction.atomic
    def save(self):
        password = self.cleaned_data.pop('password')
        u = super().save()
        u.is_budget = True
        u.set_password(password)
        u.save()
        return u


# Due process FORM
class DueProcessForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        }
    ))

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }
    ))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password'
        }
    ))

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'username', 'gender', 'password']

    @transaction.atomic
    def save(self):
        password = self.cleaned_data.pop('password')
        u = super().save()
        u.is_dueprocess = True
        u.set_password(password)
        u.save()
        return u


# PMP form
class PMPForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        }
    ))

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }
    ))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password'
        }
    ))

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'username', 'gender', 'password']

    @transaction.atomic
    def save(self):
        password = self.cleaned_data.pop('password')
        u = super().save()
        u.is_pmp = True
        u.set_password(password)
        u.save()
        return u


# USER EDIT PROFILE FORM
class EditProfileForm(UserChangeForm):

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
        }
    ))

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    password = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = (
            # 'username',
            'email',
            'first_name',
            'last_name',
            'gender',
            'password'
        )

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import UserSettings


class UserSettingsForm(forms.ModelForm):
    """Form for user settings"""
    class Meta:
        """sets which fields will be used in the form"""
        model = UserSettings
        fields = ['level']


class UserCreateForm(forms.ModelForm):
    """Form for creating new user"""
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Repeat password")

    def clean(self):
        """performs the default form validation and returns processed data"""
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidationError('Hasła muszą być takie same')
        return cleaned_data

    class Meta:
        """sets which fields will be used in the form"""
        model = User
        fields = ['username', 'email']


class LoginForm(forms.Form):
    """Form for login"""
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)

    def clean(self):
        """Authentication user"""
        cleaned_data = super().clean()
        user = authenticate(**cleaned_data)
        if user is None:
            raise ValidationError('Invalid login or password')
        cleaned_data['user'] = user



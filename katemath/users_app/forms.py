from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory

from .models import UserSettings


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = ['level']


UserSettingsFormSet = inlineformset_factory(User, UserSettings, form=UserSettingsForm,
                                            can_delete=False, max_num=2, extra=2)


class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Repeat password")
    user_settings = UserSettingsFormSet()

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidationError('Hasła muszą być takie same')
        return cleaned_data

    class Meta:
        model = User
        fields = ['username', 'email']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        user = authenticate(**cleaned_data)
        if user is None:
            raise ValidationError('Invalid login or password')
        cleaned_data['user'] = user


# class UserSettingsForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name', 'password', 'UserSettings__level']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['user_settings__level'].label = 'Field level from Model UserSettings'
#
#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         if commit:
#             instance.save()
#         return instance

# czytam by dowiedzieć sięjak łączyć formularze i jak tworzyćformularz z kilku modeli
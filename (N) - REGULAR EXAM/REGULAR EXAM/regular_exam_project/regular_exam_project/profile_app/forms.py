from django import forms
from .models import *


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel

        exclude = ['image_url', 'age']

        labels = {'first_name': '',
                  'last_name': '',
                  'email': '',
                  'password': ''}

        widgets = {'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
                   'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
                   'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
                   'password': forms.PasswordInput(attrs={'placeholder': 'Password'})}


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel

        exclude = ['email', 'password']

        labels = {'first_name': 'First Name:',
                  'last_name': 'Last Name:',
                  'image_url': 'Image URL:',
                  'age': 'Age:'}

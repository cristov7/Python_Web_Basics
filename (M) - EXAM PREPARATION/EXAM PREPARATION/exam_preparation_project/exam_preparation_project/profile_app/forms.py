from django import forms
from exam_preparation_project.profile_app.models import *


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ['profile_to_album']

        labels = {'username': 'Username:',
                  'email': 'Email:',
                  'age': 'Age:'}

        widgets = {'username': forms.TextInput(attrs={'placeholder': 'Username'}),
                   'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
                   'age': forms.NumberInput(attrs={'placeholder': 'Age'})}

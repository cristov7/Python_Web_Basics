from django import forms
from .models import ProfileModel


class CreateProfileModelModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ['first_name', 'last_name']

        widgets = {'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
                   'profile_picture': forms.URLInput(attrs={'placeholder': 'Profile Picture'}),
                   'password': forms.PasswordInput(attrs={'placeholder': 'Password'})}


class EditProfileModelModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'

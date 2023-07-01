from django import forms
from .models import *


class PetBaseModelForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo']

        labels = {'name': 'Pet Name',
                  'date_of_birth': 'Date of Birth',
                  'personal_photo': 'Link to Image'}

        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
                   'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
                   'personal_photo': forms.URLInput(attrs={'placeholder': 'Link to image'})}


class PetAddModelForm(PetBaseModelForm):
    pass


class PetEditModelForm(PetBaseModelForm):
    pass


class PetDeleteModelForm(PetBaseModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

from django import forms
from .models import *


class PhotoAddModelForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

        labels = {'photo': 'Photo file',
                  'description': 'Description',
                  'location': 'Location',
                  'tagged_pets': 'Tag Pets'}


class PhotoEditModelForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['photo']

        labels = {'description': 'Description',
                  'location': 'Location',
                  'tagged_pets': 'Tag Pets'}

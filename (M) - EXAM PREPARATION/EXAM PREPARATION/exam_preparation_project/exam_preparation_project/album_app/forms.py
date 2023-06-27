from django import forms
from exam_preparation_project.album_app.models import *


class AlbumModelForm(forms.ModelForm):
    # genre = forms.ChoiceField(choices=AlbumModel.GENRE_CHOICES)

    class Meta:
        model = AlbumModel
        fields = '__all__'

        labels = {'album_name': 'Album Name:',
                  'artist': 'Artist:',
                  'genre': 'Genre:',
                  'description': 'Description:',
                  'image_url': 'Image URL:',
                  'price': 'Price:'}

        widgets = {'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
                   'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
                   'description': forms.Textarea(attrs={'placeholder': 'Description'}),
                   'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
                   'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
                   'profile': forms.HiddenInput()}

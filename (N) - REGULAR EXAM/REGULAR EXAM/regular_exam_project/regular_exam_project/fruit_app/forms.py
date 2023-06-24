from django import forms
from .models import *


class FruitModelForm(forms.ModelForm):
    class Meta:
        model = FruitModel

        fields = '__all__'

        labels = {'name': '',
                  'image_url': '',
                  'description': '',
                  'nutrition': ''}

        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
                   'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
                   'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
                   'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
                   'profile': forms.HiddenInput()}


class EditFruitModelForm(forms.ModelForm):
    class Meta:
        model = FruitModel

        fields = '__all__'

        labels = {'name': 'Name:',
                  'image_url': 'Image URL:',
                  'description': 'Description:',
                  'nutrition': 'Nutrition:'}

        widgets = {'profile': forms.HiddenInput()}


class DeleteFruitModelForm(forms.ModelForm):
    class Meta:
        model = FruitModel

        exclude = ['nutrition', 'profile']

        labels = {'name': 'Name:',
                  'image_url': 'Image URL:',
                  'description': 'Description:'}

    def __int__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'

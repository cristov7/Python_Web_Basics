from django import forms
from .models import EventModel


class CreateEventModelModelForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = '__all__'

        labels = {'event_name': 'Name'}

        widgets = {'event_name': forms.TextInput(attrs={'placeholder': 'Name'}),
                   'description': forms.Textarea(attrs={'placeholder': 'Description'}),
                   'date': forms.DateInput(attrs={'placeholder': 'Date'}),
                   'event_image': forms.URLInput(attrs={'placeholder': 'Event Image'}),
                   'profile': forms.HiddenInput()}


class EditEventModelModelForm(CreateEventModelModelForm):
    pass


class DeleteEventModelModelForm(CreateEventModelModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

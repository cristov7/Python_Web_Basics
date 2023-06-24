from django import forms
from django.core import validators
from .validators import min_value_validator_func, max_value_validator_func, ValueInRangeValidator
from .models import TodoModel, ImageModel, DocumentModel


# Form validation happens when the data is cleaned:
# ▪ Raises ValidationError and passes the relevant information
# ▪ Returns the normalized (cleaned) data as a Python object
# Each form field has a custom validation logic

# You can pass additional validators to a Form field
# You can use both:
# - Built-in Django validators
# - Custom validators


class TodoForm(forms.Form):
    text = forms.CharField(
        validators=[
            # Built-in Django validators:
            validators.MinLengthValidator(5),      # len(text) >= 5
            validators.MaxLengthValidator(100)],   # len(text) <= 100
            # Error Messages in Forms (because of built-in Django validators):
            error_messages={'required': 'This field is REQUIRED!',
                            'min_length': 'Invalid MIN length!'})

    done = forms.BooleanField(required=False)

    priority = forms.IntegerField(
        validators=[
            # Custom function validators:     # Built-in Django validators:
            # min_value_validator_func,       # validators.MinValueValidator(1),
            # max_value_validator_func])      # validators.MaxValueValidator(10)

            # Custom class validator:
            ValueInRangeValidator(1, 10)])

    # Error Messages in Forms:
    # error_messages={'priority': 'Invalid priority!'})

    # Override the 'clean()' method:
    def clean(self):   # 'clean' all clean methods ('clean_text', 'clean_done', 'clean_priority')
        cleaned_data = super().clean()
        return cleaned_data

    def clean_text(self):   # 'clean' key word + 'text' form field
        text = self.cleaned_data['text']

        # Additional clean method:
        if 'bad' in text.lower():
            raise validators.ValidationError('Bad word detected!')

        # Normalize the 'text' value:
        return text.lower()

    def clean_done(self):  # 'clean' key word + 'done' form field
        done = self.cleaned_data['done']
        return done

    def clean_priority(self):  # 'clean' key word + 'priority' form field
        priority = self.cleaned_data['priority']
        return priority


class TodoModelForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = '__all__'

        widgets = {'text': forms.TextInput(attrs={'placeholder': 'text'}),
                   'priority': forms.TextInput(attrs={'placeholder': 'priority'})}

        # Error Messages in ModelForms:
        error_messages = {'text': {'required': 'This field is REQUIRED!'}}


class ImageModelForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'


class DocumentModelForm(forms.ModelForm):
    class Meta:
        model = DocumentModel
        fields = '__all__'

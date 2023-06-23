from django import forms
from .models import Person


class PersonForm(forms.Form):
    # -> Form Field Arguments: by default, each Field class assumes the value is required

    # 'required=False' == 'blank=True' + 'null = True'
    # 'required=True' == 'blank=False' + 'null = False'

    name = forms.CharField(label='First Name')
    # 'label' == 'verbose_name'

    age = forms.IntegerField(initial=18)
    # 'initial' == 'default'

    # description = forms.CharField(help_text='Additional information about yourself!')
    # 'help_text': it will be displayed next to the field

    # -> Built - in Widgets: widgets give you the opportunity to set HTML attributes using Python code

    # comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 10, 'placeholder': 'comment'}))
    # 'forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 10, 'placeholder': 'comment'}))':
    # You can specify a form that uses a larger Textarea widget

    # info = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'info'}))
    # 'forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'info'}))':
    # CharField uses TextInput widget by default

    # number = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'number'}))

    # email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'email'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

    # url = forms.URLField(widget=forms.URLInput(attrs={'placeholder': 'url'}))

    # date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'date'}))

    # date_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placeholder': 'date and time'}))

    # -> Select, Checkbox and Radio Button:

    # CHOICES = (('Man Utd', 'Man Utd'),
    #            ('Real M', 'Real M'),
    #            ('Bayern', 'Bayern'))

    # Select List Widget: Select is the default widget for ChoiceField
    # A select list allows you to choose options from a drop-down menu
    # select_list_1 = forms.ChoiceField(choices=CHOICES)
    # select_list_2 = forms.CharField(widget=forms.Select(choices=CHOICES))

    # Checkbox Widget: CheckboxInput is the default widget for BooleanField
    # A checkbox allows you to select options from a list of options
    # checkbox = forms.BooleanField(required=False)
    # checkbox_multiple = forms.CharField(widget=forms.CheckboxSelectMultiple(choices=CHOICES))

    # Radio Button Widget: RadioSelect is similar to the Django Select widget
    # A radio button - allows you to select only one option from a list of options
    # radio_button_1 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    # radio_button_2 = forms.CharField(widget=forms.RadioSelect(choices=CHOICES))


class PersonModelForm(forms.ModelForm):   # 'ModelForm': Convert a model into a form and directly add or edit a model
    class Meta:
        model = Person               # Specify the model you want to create a form for
        # fields = '__all__'         # add all the created model fields
        fields = ['name', 'age']     # set the fields that will be edited in the form
        # exclude = ['password']     # fields to be excluded from the form

        # Overriding the Default Fields:

        # You have the flexibility of changing the field type for the model:
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'full name'}),
                   'age': forms.NumberInput(attrs={'placeholder': 'age'})}

        # You can specify a different label for a field:
        labels = {'name': 'Full Name',
                  'age': 'Age'}

        # You can add a help text for a field:
        help_texts = {'name': 'You must supply valid full name!',
                      'age': 'You must supply valid age!'}

        # error_messages = {'__all__': 'It is important to be a valid data!'}

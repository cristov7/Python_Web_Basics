from django.db import models
from django.core.validators import MinLengthValidator
from petstagram.pets.models import *
from .validators import *


class Photo(models.Model):
    # To work with an image field, we should install a library called Pillow: 'pip install Pillow'
    photo = models.ImageField(validators=(validate_file_size,), upload_to='photos')
    description = models.TextField(max_length=300, validators=(MinLengthValidator(10),), blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.photo}'

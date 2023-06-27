from django.db import models
from django.core import validators
from .validators import *
from exam_preparation_project.album_app.models import *


class ProfileModel(models.Model):
    username = models.CharField(blank=False, null=False,
                                validators=[validators.MinLengthValidator(2),
                                            consist_only_of_letters_numbers_and_underscore_func],
                                max_length=15)

    email = models.EmailField(blank=False, null=False)

    age = models.IntegerField(blank=True, null=True,
                              validators=[validators.MinValueValidator(0)])

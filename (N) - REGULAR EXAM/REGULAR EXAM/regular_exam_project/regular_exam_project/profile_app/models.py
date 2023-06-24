from django.db import models
from django.core import validators
from .validator import *


class ProfileModel(models.Model):
    first_name = models.CharField(blank=False, null=False,
                                  max_length=25,
                                  validators=[validators.MinLengthValidator(2),
                                              start_with_a_letter_validator])

    last_name = models.CharField(blank=False, null=False,
                                 max_length=35,
                                 validators=[validators.MinLengthValidator(1),
                                             start_with_a_letter_validator])

    email = models.EmailField(blank=False, null=False,
                              max_length=40)

    password = models.CharField(blank=False, null=False,
                                max_length=20,
                                validators=[validators.MinLengthValidator(8)])

    image_url = models.URLField(blank=True, null=True)

    age = models.IntegerField(blank=True, null=True,
                              default=18)

    @property   # getter
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

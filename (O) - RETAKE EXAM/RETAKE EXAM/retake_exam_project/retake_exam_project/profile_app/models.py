from django.db import models
from .validators import consist_only_of_letters_func, contain_at_least_one_digit_func
from django.core import validators


class ProfileModel(models.Model):
    first_name = models.CharField(blank=True, null=True,
                                  max_length=20,
                                  validators=[consist_only_of_letters_func])

    last_name = models.CharField(blank=True, null=True,
                                 validators=[validators.MinLengthValidator(4)],
                                 max_length=30)

    email = models.EmailField(blank=False, null=False,
                              max_length=45)

    profile_picture = models.URLField(blank=True, null=True)

    password = models.CharField(blank=False, null=False,
                                validators=[validators.MinLengthValidator(5),
                                            contain_at_least_one_digit_func],
                                max_length=20)

    @property   # getter
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

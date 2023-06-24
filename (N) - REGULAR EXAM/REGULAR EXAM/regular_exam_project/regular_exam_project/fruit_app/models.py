from django.db import models
from django.core import validators
from .validator import *
from regular_exam_project.profile_app.models import *


class FruitModel(models.Model):
    name = models.CharField(blank=False, null=False,
                            max_length=30,
                            validators=[validators.MinLengthValidator(2),
                                        contain_only_letter_validator])

    image_url = models.URLField(blank=False, null=False)

    description = models.TextField(blank=False, null=False)

    nutrition = models.TextField(blank=True, null=True)

    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)

from django.db import models
from django.core import validators
from exam_preparation_project.profile_app.models import *


class AlbumModel(models.Model):
    album_name = models.CharField(blank=False, null=False,
                                  unique=True,
                                  max_length=30)

    artist = models.CharField(blank=False, null=False,
                              max_length=30)

    GENRE_CHOICES = [('Pop Music', 'Pop Music'),
                     ('Jazz Music', 'Jazz Music'),
                     ('R&B Music', 'R&B Music'),
                     ('Rock Music', 'Rock Music'),
                     ('Country Music', 'Country Music'),
                     ('Dance Music', 'Dance Music'),
                     ('Hip Hop Music', 'Hip Hop Music'),
                     ('Other', 'Other')]

    genre = models.CharField(blank=False, null=False,
                             max_length=30,
                             choices=GENRE_CHOICES)

    description = models.TextField(blank=True, null=True)

    image_url = models.URLField(blank=False, null=False)

    price = models.FloatField(blank=False, null=False,
                              validators=[validators.MinValueValidator(0)])

    # Many-to-One Relationship:
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)

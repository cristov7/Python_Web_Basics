from django.db import models
from django.core import validators
from .validators import prevent_users_from_selecting_a_date_earlier_than_today_func
from retake_exam_project.profile_app.models import ProfileModel


class EventModel(models.Model):
    event_name = models.CharField(blank=False, null=False,
                                  validators=[validators.MinLengthValidator(2)],
                                  max_length=30)

    CATEGORY_CHOICES = (('Sports', 'Sports'),
                        ('Festivals', 'Festivals'),
                        ('Conferences', 'Conferences'),
                        ('Performing Art', 'Performing Art'),
                        ('Concerts', 'Concerts'),
                        ('Theme Party', 'Theme Party'),
                        ('Other', 'Other'))

    category = models.CharField(blank=False, null=False,
                                choices=CATEGORY_CHOICES,
                                max_length=14)

    description = models.TextField(blank=True, null=True)

    date = models.DateField(blank=False, null=False,
                            validators=[prevent_users_from_selecting_a_date_earlier_than_today_func])

    event_image = models.URLField(blank=False, null=False)

    # Many - to - One Relationship: Many EventModel objects can have only One ProfileModel object
    profile = models.ForeignKey(to=ProfileModel, on_delete=models.CASCADE)

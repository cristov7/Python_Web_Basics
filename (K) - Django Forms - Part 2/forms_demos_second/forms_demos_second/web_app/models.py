from django.db import models
from .validators import min_value_validator_func, max_value_validator_func


class TodoModel(models.Model):
    text = models.CharField(max_length=100,
                            # Error Messages in Models:)
                            error_messages={'unique': 'This text must be UNIQUE!'})

    done = models.BooleanField(default=False)

    priority = models.IntegerField(
        validators=[
            # Custom function validators:
            min_value_validator_func,
            max_value_validator_func])


class ImageModel(models.Model):
    # upload_to='images': name of the folder where the images will be stored
    image = models.ImageField(upload_to='images')

    description = models.CharField(max_length=100)


class DocumentModel(models.Model):
    # upload_to='documents': name of the folder where the images will be stored
    documents = models.FileField(upload_to='documents')

    description = models.CharField(max_length=100)

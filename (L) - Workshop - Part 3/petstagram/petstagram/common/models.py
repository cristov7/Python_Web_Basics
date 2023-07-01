from django.db import models
from petstagram.photos.models import *


class Comment(models.Model):

    class Meta:
        ordering = ['-date_time_of_publication']

    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.text}'


class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.to_photo}'

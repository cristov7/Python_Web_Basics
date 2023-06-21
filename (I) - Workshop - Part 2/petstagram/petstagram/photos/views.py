from django.shortcuts import render
from .models import Photo


def photo_add(request):
    template_name = 'photos/photo-add-page.html'
    return render(request, template_name)


def photo_details(request, pk: int):
    template_name = 'photos/photo-details-page.html'

    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()

    context = {'photo': photo,
               'likes': likes,
               'comments': comments}

    return render(request, template_name, context)


def photo_edit(request, pk: int):
    template_name = 'photos/photo-edit-page.html'
    return render(request, template_name)

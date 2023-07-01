from django.shortcuts import render, redirect
from .models import *
from .forms import *
from petstagram.common.forms import *


def photo_add(request):
    template_name = 'photos/photo-add-page.html'

    if request.method == 'POST':
        model_form = PhotoAddModelForm(request.POST, request.FILES)

        if model_form.is_valid():
            model_form.save()
            return redirect('index')

    else:   # request.method == 'GET':
        model_form = PhotoAddModelForm()

    context = {'model_form': model_form}

    return render(request, template_name, context)


def photo_details(request, pk: int):
    template_name = 'photos/photo-details-page.html'

    photo_object = Photo.objects.get(pk=pk)
    all_like_objects = photo_object.like_set.all()
    all_comment_objects = photo_object.comment_set.all()

    context = {'photo_object': photo_object,
               'all_like_objects': all_like_objects,
               'all_comment_objects': all_comment_objects,
               'comment_form': CommentModelForm()}

    return render(request, template_name, context)


def photo_edit(request, pk: int):
    template_name = 'photos/photo-edit-page.html'

    photo_object = Photo.objects.get(pk=pk)

    if request.method == 'POST':
        model_form = PhotoEditModelForm(request.POST, instance=photo_object)

        if model_form.is_valid():
            model_form.save()
            return redirect('photo details', pk=pk)

    else:   # request.method == 'GET':
        model_form = PhotoEditModelForm(instance=photo_object)

    context = {'model_form': model_form}

    return render(request, template_name, context)


def photo_delete(request, pk: int):
    photo_object = Photo.objects.get(pk=pk)

    photo_object.delete()

    return redirect('index')

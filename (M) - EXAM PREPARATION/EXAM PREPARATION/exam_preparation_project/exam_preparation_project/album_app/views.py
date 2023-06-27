from django.http import HttpRequest
from exam_preparation_project.album_app.forms import *
from exam_preparation_project.album_app.models import *
from django.shortcuts import render, redirect


def add_album_page_func(request: HttpRequest):
    template_name = 'album_app/add-album.html'

    if request.method == 'POST':

        request_data = request.POST.copy()
        request_data['profile'] = ProfileModel.objects.first().pk
        form = AlbumModelForm(request_data)

        if form.is_valid():
            form.save()
            return redirect('home page')

    else:   # request.method == 'GET':
        form = AlbumModelForm()

    context = {'form': form}

    return render(request, template_name, context)


def album_details_page_func(request: HttpRequest, pk: int):
    template_name = 'album_app/album-details.html'

    album_object = AlbumModel.objects.get(pk=pk)

    context = {'album_image': album_object.image_url,
               'name': album_object.album_name,
               'artist': album_object.artist,
               'genre': album_object.genre,
               'price': f'{album_object.price:.2f}',
               'description': album_object.description,
               'pk': album_object.pk}

    return render(request, template_name, context)


def edit_album_page_func(request: HttpRequest, pk: int):
    template_name = 'album_app/edit-album.html'

    album_object = AlbumModel.objects.get(pk=pk)

    if request.method == 'POST':
        form = AlbumModelForm(request.POST, instance=album_object)

        if form.is_valid():
            form.save()
            return redirect('home page')

    else:   # request.method == 'GET':
        form = AlbumModelForm(instance=album_object)

    context = {'form': form}

    return render(request, template_name, context)


def delete_album_page_func(request: HttpRequest, pk: int):
    template_name = 'album_app/delete-album.html'

    album_object = AlbumModel.objects.get(pk=pk)

    if request.method == 'POST':
        form = AlbumModelForm(request.POST, instance=album_object)

        if form.is_valid():
            album_object.delete()
            return redirect('home page')

    else:   # request.method == 'GET':
        form = AlbumModelForm(instance=album_object)

    context = {'form': form}

    return render(request, template_name, context)

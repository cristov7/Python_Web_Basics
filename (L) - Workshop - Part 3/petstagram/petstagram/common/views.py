from django.shortcuts import render, redirect, resolve_url
from petstagram.photos.models import *
from .models import *
from pyperclip import copy
from .forms import *


def index(request):
    template_name = 'common/home-page.html'

    all_photo_objects = Photo.objects.all()
    comment_form = CommentModelForm()
    search_form = SearchForm()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)

        if search_form.is_valid():
            all_photo_objects = all_photo_objects.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

    context = {'all_photo_objects': all_photo_objects,
               'comment_form': comment_form,
               'search_form': search_form}

    return render(request, template_name, context)


def like_functionality(request, photo_id: int):
    photo = Photo.objects.get(pk=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(f'http://localhost:8000/#{photo_id}')
    # return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
    #                 request.META['HTTP_REFERER'] == 'http://localhost:8000/'


def share_functionality(request, photo_id: int):
    copy(f'http://127.0.0.1:8000/photos/{photo_id}/')
    # copy(request.META['HTTP_REFERER'] + resolve_url('photo details', pk=photo_id))
    #                  ['HTTP_REFERER'] == 'http://localhost:8000/'

    return redirect(f'http://localhost:8000/#{photo_id}')
    # return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
    #                 request.META['HTTP_REFERER'] == 'http://localhost:8000/'


def comment_functionality(request, photo_id: int):
    photo_object = Photo.objects.get(pk=photo_id)

    if request.method == 'POST':
        model_form = CommentModelForm(request.POST)

        if model_form.is_valid():
            comment_object = model_form.save(commit=False)
            comment_object.to_photo = photo_object
            comment_object.save()

        return redirect(f'http://localhost:8000/#{photo_id}')
        # return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
        #                 request.META['HTTP_REFERER'] == 'http://localhost:8000/'

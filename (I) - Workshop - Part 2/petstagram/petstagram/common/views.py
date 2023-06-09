from django.shortcuts import render, redirect, resolve_url
from petstagram.photos.models import Photo
from .models import Like
from pyperclip import copy


def index(request):
    template_name = 'common/home-page.html'
    context = {'all_photos': Photo.objects.all()}

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

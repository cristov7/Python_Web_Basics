from django.http import HttpRequest
from exam_preparation_project.profile_app.models import *
from exam_preparation_project.profile_app.forms import *
from django.shortcuts import render, redirect


def home_page_func(request: HttpRequest):
    template_name = 'my_music_app/'

    context = {}

    profile_object = ProfileModel.objects.first()

    if profile_object:
        template_name += 'home-with-profile.html'

        context['profile_object'] = profile_object
        context['all_album_objects'] = profile_object.albummodel_set.all()

    else:
        template_name += 'home-no-profile.html'

    if request.method == 'POST':
        form = ProfileModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home page')

    else:  # request.method == 'GET':
        form = ProfileModelForm()

    context['form'] = form

    return render(request, template_name, context)

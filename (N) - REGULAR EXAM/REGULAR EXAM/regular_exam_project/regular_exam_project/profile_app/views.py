from django.http import HttpRequest
from .forms import *
from regular_exam_project.profile_app.templatetags.custom_tags import profile_status
from django.shortcuts import render, redirect


def profile_create_page_func(request: HttpRequest):
    template_name = 'profile_app/create-profile.html'

    if request.method == 'POST':
        form = ProfileModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    else:   # request.method == 'GET':
        form = ProfileModelForm()

    context = {'form': form}

    return render(request, template_name, context)


def profile_details_page_func(request: HttpRequest):
    template_name = 'profile_app/details-profile.html'
    return render(request, template_name)


def profile_edit_page_func(request: HttpRequest):
    template_name = 'profile_app/edit-profile.html'

    form = EditProfileModelForm(request.POST or None, instance=profile_status())

    if form.is_valid():
        form.save()
        return redirect('profile details page')

    context = {'form': form}

    return render(request, template_name, context)


def profile_delete_page_func(request: HttpRequest):
    template_name = 'profile_app/delete-profile.html'

    profile_object = profile_status()

    if request.method == 'POST':
        profile_object.delete()
        return redirect('index page')

    return render(request, template_name)

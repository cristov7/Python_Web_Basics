from django.http import HttpRequest
from exam_preparation_project.profile_app.models import *
from exam_preparation_project.profile_app.forms import *
from django.shortcuts import render, redirect


def profile_details_page_func(request: HttpRequest):
    template_name = 'profile_app/profile-details.html'

    profile_object = ProfileModel.objects.first()

    context = {'username': profile_object.username,
               'email': profile_object.email,
               'age': profile_object.age,
               'albums': profile_object.albummodel_set.count()}

    return render(request, template_name, context)


def delete_profile_page_func(request: HttpRequest):
    template_name = 'profile_app/profile-delete.html'

    profile_object = ProfileModel.objects.first()

    if request.method == 'POST':
        profile_object.delete()
        return redirect('home page')

    return render(request, template_name)

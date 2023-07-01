from django.shortcuts import render, redirect
from .models import *
from .forms import *


def pet_add(request):
    template_name = 'pets/pet-add-page.html'

    if request.method == 'POST':
        model_form = PetAddModelForm(request.POST)

        if model_form.is_valid():
            model_form.save()
            return redirect('profile details', pk=1)

    else:   # request.method == 'GET':
        model_form = PetAddModelForm()

    context = {'model_form': model_form}

    return render(request, template_name, context)


def pet_details(request, username: str, pet_name):
    template_name = 'pets/pet-details-page.html'

    pet_object = Pet.objects.get(slug=pet_name)
    all_photo_objects = pet_object.photo_set.all()

    context = {'pet_object': pet_object,
               'all_photo_objects': all_photo_objects}

    return render(request, template_name, context)


def pet_edit(request, username: str, pet_name):
    template_name = 'pets/pet-edit-page.html'

    pet_object = Pet.objects.get(slug=pet_name)

    if request.method == 'POST':
        model_form = PetEditModelForm(request.POST, instance=pet_object)

        if model_form.is_valid():
            model_form.save()
            return redirect('pet details', username=username, pet_name=pet_name)

    else:
        model_form = PetEditModelForm(instance=pet_object)

    context = {'model_form': model_form}

    return render(request, template_name, context)


def pet_delete(request, username: str, pet_name):
    template_name = 'pets/pet-delete-page.html'

    pet_object = Pet.objects.get(slug=pet_name)

    if request.method == 'POST':
        pet_object.delete()
        return redirect('profile details', pk=1)

    else:   # request.method == 'GET':
        model_form = PetDeleteModelForm(instance=pet_object)

    context = {'model_form': model_form}

    return render(request, template_name, context)

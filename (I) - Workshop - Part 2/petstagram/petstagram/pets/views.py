from django.shortcuts import render
from .models import Pet


def pet_add(request):
    template_name = 'pets/pet-add-page.html'
    return render(request, template_name)


def pet_details(request, username: str, pet_name):
    template_name = 'pets/pet-details-page.html'

    pet = Pet.objects.get(slug=pet_name)
    all_photos = pet.photo_set.all()

    context = {'pet': pet,
               'all_photos': all_photos}

    return render(request, template_name, context)


def pet_edit(request, username: str, pet_name):
    template_name = 'pets/pet-edit-page.html'
    return render(request, template_name)


def pet_delete(request, username: str, pet_name):
    template_name = 'pets/pet-delete-page.html'
    return render(request, template_name)

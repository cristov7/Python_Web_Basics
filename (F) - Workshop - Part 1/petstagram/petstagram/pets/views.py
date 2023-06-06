from django.shortcuts import render

# Create your views here.


def pet_add(request):
    template_name = 'pets/pet-add-page.html'
    return render(request, template_name)


def pet_details(request, username: str, pet_name):
    template_name = 'pets/pet-details-page.html'
    return render(request, template_name)


def pet_edit(request, username: str, pet_name):
    template_name = 'pets/pet-edit-page.html'
    return render(request, template_name)


def pet_delete(request, username: str, pet_name):
    template_name = 'pets/pet-delete-page.html'
    return render(request, template_name)

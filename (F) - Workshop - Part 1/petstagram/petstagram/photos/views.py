from django.shortcuts import render

# Create your views here.


def photo_add(request):
    template_name = 'photos/photo-add-page.html'
    return render(request, template_name)


def photo_details(request, pk: int):
    template_name = 'photos/photo-details-page.html'
    return render(request, template_name)


def photo_edit(request, pk: int):
    template_name = 'photos/photo-edit-page.html'
    return render(request, template_name)

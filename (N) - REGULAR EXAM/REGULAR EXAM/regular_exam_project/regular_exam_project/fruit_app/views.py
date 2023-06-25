from django.http import HttpRequest
from regular_exam_project.fruit_app.forms import *
from regular_exam_project.profile_app.templatetags.custom_tags import profile_status
from django.shortcuts import render, redirect


def fruit_create_page_func(request: HttpRequest):
    template_name = 'fruit_app/create-fruit.html'

    profile_object = profile_status()

    if request.method == 'POST':
        data = request.POST.copy()
        data['profile'] = profile_object.pk

        form = FruitModelForm(data)

        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    else:   # request.method == 'GET':
        form = FruitModelForm()

    context = {'form': form}

    return render(request, template_name, context)


def fruit_details_page_func(request: HttpRequest, pk: int):
    template_name = 'fruit_app/details-fruit.html'
    context = {'fruit_object': FruitModel.objects.get(pk=pk)}
    return render(request, template_name, context)


def fruit_edit_page_func(request: HttpRequest, pk: int):
    template_name = 'fruit_app/edit-fruit.html'

    fruit_object = FruitModel.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditFruitModelForm(request.POST, instance=fruit_object)

        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    else:   # request.method == 'GET':
        form = EditFruitModelForm(instance=fruit_object)

    context = {'form': form}

    return render(request, template_name, context)


def fruit_delete_page_func(request: HttpRequest, pk: int):
    template_name = 'fruit_app/delete-fruit.html'

    fruit_object = FruitModel.objects.get(pk=pk)

    if request.method == 'POST':
        fruit_object.delete()
        return redirect('dashboard page')

    context = {'form': DeleteFruitModelForm(instance=fruit_object)}

    return render(request, template_name, context)

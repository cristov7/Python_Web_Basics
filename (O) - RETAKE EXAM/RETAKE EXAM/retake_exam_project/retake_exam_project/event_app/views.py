from django.http import HttpRequest
from .models import ProfileModel, EventModel
from django.shortcuts import render, redirect
from .forms import CreateEventModelModelForm, EditEventModelModelForm, DeleteEventModelModelForm


def home_func(request: HttpRequest):
    template_name = 'shared/home-page.html'

    profile_object = ProfileModel.objects.first()

    context = {'profile_object': profile_object}

    return render(request, template_name, context)


def dashboard_func(request: HttpRequest):
    template_name = 'event_app/events-dashboard.html'

    profile_object = ProfileModel.objects.first()
    all_event_objects = profile_object.eventmodel_set.all()

    context = {'profile_object': profile_object,
               'all_event_objects': all_event_objects}

    return render(request, template_name, context)


def create_event_func(request: HttpRequest):
    template_name = 'event_app/event-create.html'

    profile_object = ProfileModel.objects.first()

    if request.method == 'POST':
        request_post = request.POST.copy()
        request_post['profile'] = profile_object.pk

        model_form = CreateEventModelModelForm(request_post)

        if model_form.is_valid():
            model_form.save()

            return redirect('dashboard page')

    else:   # request.method == 'GET':
        model_form = CreateEventModelModelForm()

    context = {'profile_object': profile_object,
               'model_form': model_form}

    return render(request, template_name, context)


def event_details_func(request: HttpRequest, pk: int):
    template_name = 'event_app/event-details.html'

    profile_object = ProfileModel.objects.first()
    event_object = EventModel.objects.get(pk=pk)

    context = {'profile_object': profile_object,
               'event_object': event_object}

    return render(request, template_name, context)


def edit_event_func(request: HttpRequest, pk: int):
    template_name = 'event_app/event-edit.html'

    profile_object = ProfileModel.objects.first()
    event_object = EventModel.objects.get(pk=pk)

    if request.method == 'POST':
        model_form = EditEventModelModelForm(request.POST, instance=event_object)

        if model_form.is_valid():
            model_form.save()

            return redirect('dashboard page')

    else:   # request.method == 'GET':
        model_form = EditEventModelModelForm(instance=event_object)

    context = {'profile_object': profile_object,
               'event_object': event_object,
               'model_form': model_form}

    return render(request, template_name, context)


def delete_event_func(request: HttpRequest, pk: int):
    template_name = 'event_app/event-delete.html'

    profile_object = ProfileModel.objects.first()
    event_object = EventModel.objects.get(pk=pk)

    if request.method == 'POST':
        event_object.delete()

        return redirect('dashboard page')

    else:   # request.method == 'GET':
        model_form = DeleteEventModelModelForm(instance=event_object)

    context = {'profile_object': profile_object,
               'event_object': event_object,
               'model_form': model_form}

    return render(request, template_name, context)

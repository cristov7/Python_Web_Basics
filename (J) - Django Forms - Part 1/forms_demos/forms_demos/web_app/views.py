from django.http import HttpRequest
from .forms import PersonForm, PersonModelForm
from .models import Person
from django.shortcuts import render, get_object_or_404


def index_func(request: HttpRequest):
    template_name = 'web_app/index.html'

    name = None
    age = None
    password = None

    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():   # validate the form

            # '.cleaned_data' is generated after '.is_valid()'
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            password = len(form.cleaned_data['password']) * '*'

            # Create model from cleaned data:
            form_dict = form.cleaned_data   # {'name': name, 'age': age, 'password': password}
            Person.objects.create(**form_dict)                       # save to database
            # Person(name=name, age=age, password=password).save()   # save to database

    else:   # if request.method == 'GET':
        form = PersonForm()

    context = {'form': form,

               'name': name,
               'age': age,
               'password': password}

    return render(request, template_name, context)


def model_form_func(request: HttpRequest, pk: int):
    template_name = 'web_app/model_form.html'

    person_obj = get_object_or_404(Person, pk=pk)

    if request.method == "POST":
        form = PersonModelForm(request.POST, instance=person_obj)

        if form.is_valid():
            form.save()   # update data
            # redirect to the desired page

    else:   # if request.method == "GET":
        form = PersonModelForm(instance=person_obj)

    context = {'form': form,
               'person_obj': person_obj}
    return render(request, template_name, context)

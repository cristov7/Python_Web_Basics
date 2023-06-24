from django.http import HttpRequest
from .forms import TodoForm, TodoModelForm, ImageModelForm, DocumentModelForm
from .models import TodoModel, ImageModel, DocumentModel
from django.shortcuts import render


def index_func(request: HttpRequest):
    template_name = 'web_app/index.html'

    if request.method == 'POST':
        # form = TodoForm(request.POST)
        model_form = TodoModelForm(request.POST)

        if model_form.is_valid():
            model_form_dict = model_form.cleaned_data
            print(model_form_dict)

            # Save to database:
            TodoModel(**model_form_dict).save()
            # TodoModel.objects.create(**model_form_dict)

        # if form.is_valid():
            # form_dict = form.cleaned_data
            # print(form_dict)

    else:   # if request.method == 'GET':
        # form = TodoForm()
        model_form = TodoModelForm()

    context = {
        # 'form': form,
        'model_form': model_form
    }
    return render(request, template_name, context)


def image_view_func(request: HttpRequest):
    template_name = 'web_app/image.html'

    if request.method == 'POST':
        image_form = ImageModelForm(request.POST, request.FILES)   # Handling the POST Request

        if image_form.is_valid():
            image = image_form.save()
            image.save()

    else:
        image_form = ImageModelForm()

    context = {'image_form': image_form,
               'all_image_objects': ImageModel.objects.all()}

    return render(request, template_name, context)


def document_view_func(request: HttpRequest):
    template_name = 'web_app/document.html'

    if request.method == 'POST':
        document_form = DocumentModelForm(request.POST, request.FILES)   # Handling the POST Request

        if document_form.is_valid():
            document = document_form.save()
            document.save()

    else:
        document_form = DocumentModelForm()

    context = {'document_form': document_form,
               'all_document_objects': DocumentModel.objects.all()}

    return render(request, template_name, context)

from django.http import HttpRequest
from django.shortcuts import render


def index_page_func(request: HttpRequest):
    template_name = 'fruitipedia_app/index.html'
    context = {}
    return render(request, template_name, context)


def dashboard_page_func(request: HttpRequest):
    template_name = 'fruitipedia_app/dashboard.html'
    context = {}
    return render(request, template_name, context)

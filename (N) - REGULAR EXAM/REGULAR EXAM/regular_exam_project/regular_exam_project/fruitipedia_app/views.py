from django.http import HttpRequest
from regular_exam_project.profile_app.templatetags.custom_tags import profile_status
from django.shortcuts import render


def index_page_func(request: HttpRequest):
    template_name = 'fruitipedia_app/index.html'
    return render(request, template_name)


def dashboard_page_func(request: HttpRequest):
    template_name = 'fruitipedia_app/dashboard.html'
    return render(request, template_name)

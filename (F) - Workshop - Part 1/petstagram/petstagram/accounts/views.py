from django.shortcuts import render

# Create your views here.


def register_user(request):
    template_name = 'accounts/register-page.html'
    return render(request, template_name)


def login_user(request):
    template_name = 'accounts/login-page.html'
    return render(request, template_name)


def profile_details(request, pk: int):
    template_name = 'accounts/profile-details-page.html'
    return render(request, template_name)


def profile_edit(request, pk: int):
    template_name = 'accounts/profile-edit-page.html'
    return render(request, template_name)


def profile_delete(request, pk: int):
    template_name = 'accounts/profile-delete-page.html'
    return render(request, template_name)

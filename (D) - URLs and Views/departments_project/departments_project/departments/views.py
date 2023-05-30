from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.


def index(request):                      # receive request from 'path('', index)':
    print(f'Print request: {request}')   # Print request: <WSGIRequest: GET '/departments/'>
    return HttpResponse('index')         # return response on the 'http://127.0.0.1:8000/departments/': index

    # return redirect('https://www.google.bg/')
    # # return response on the 'http://127.0.0.1:8000/departments/'


def details(request, department_id):           # receive request from 'path('<int:department_id>/', details)':
    print(f'Print request: {request}')         # Print request: <WSGIRequest: GET '/departments/1/'>
    print(f'Department ID: {department_id}')   # Department ID: 1
    print(f'Type ID: {type(department_id)}')   # Type ID: <class 'int'>

    # return HttpResponse('details')
    # # return response on the 'http://127.0.0.1:8000/departments/1/': details

    department_dict = {1: 'Developer',
                       2: 'QA'}

    response = ""

    if department_id in department_dict.keys():
        response = f'Department: {department_dict[department_id]}'
    else:
        response = 'Unknown Department'

    return HttpResponse(response)
    # return response on the 'http://127.0.0.1:8000/departments/1'
    # return response on the 'http://127.0.0.1:8000/departments/2'
    # return response on the 'http://127.0.0.1:8000/departments/3'

    # return redirect('https://www.google.bg/')
    # # return response on the 'http://127.0.0.1:8000/departments/1'
    # # return response on the 'http://127.0.0.1:8000/departments/2'
    # # return response on the 'http://127.0.0.1:8000/departments/3'


def details_template(request, department_id):   # receive request from 'path('template/<int:department_id>/', details_template)':
    department_dict = {1: 'Developer', 2: 'QA'}

    response = ""

    if department_id in department_dict.keys():
        response = f'Department: {department_dict[department_id]}'
    else:
        response = 'Unknown Department'

    context = {'title': 'Departments title from context',
               'response': response}

    return render(request, 'departments/details.html', context=context)
    # return response on the 'http://127.0.0.1:8000/departments/template/1/'
    # return response on the 'http://127.0.0.1:8000/departments/template/2/'
    # return response on the 'http://127.0.0.1:8000/departments/template/3/'

    # return redirect('https://www.google.bg/')
    # # return response on the 'http://127.0.0.1:8000/departments/template/1/'
    # # return response on the 'http://127.0.0.1:8000/departments/template/2/'
    # # return response on the 'http://127.0.0.1:8000/departments/template/3/'


def details_error(request, department_id):   # receive request from 'path('error/<int:department_id>/', details_error)':
    if department_id == 1:
        return HttpResponse('error')
        # return response on the 'http://127.0.0.1:8000/departments/error/1/'

    elif department_id == 2:
        return HttpResponseNotFound('Sorry!')
        # return response on the 'http://127.0.0.1:8000/departments/error/2/'

    elif department_id == 3:
        return HttpResponse('error status', status=404)
        # return response on the 'http://127.0.0.1:8000/departments/error/3/'

    else:
        raise Http404
        # return response on the 'http://127.0.0.1:8000/departments/error/4/'

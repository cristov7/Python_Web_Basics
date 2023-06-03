from django.shortcuts import render, redirect
import datetime

# Create your views here.


class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


some_student = Student('John', 20)


def index(request):
    template_name = 'examples/index.html'

    context = {
        'title': 'Home',
        # context['title'] = 'Home'
        # .html: {{title}} = 'Home'
        # .html {{title|upper}} = 'HOME'
        # .html {{title|lower}} = 'home'
        # .html {{title|length}} = 4
        # .html: {{title|truncatechars:2}} = H...

        'key': {'nested_key': 'nested value'},
        # context['key']['nested_key'] = 'nested value'
        # .html: {{key.nested_key}} = 'nested value'
        # .html: {{key.nested_key|capfirst}} = 'Nested value'
        # .html: {{key.nested_key|truncatewords:1}} = nested ...

        'student_age': some_student.age,
        # context['student_age'] = 20
        # .html: {{student_age}} = 20

        'students_list': ['Kalin', 'Ivan', 'Peter'],
        # ', '.join(context['students_list']) = Kalin, Ivan, Peter
        # .html: {{students_list|join:', '}} = Kalin, Ivan, Peter

        'empty_students_list': [],
        # context['empty_students_list'] = []
        # .html: {{empty_students_list}} = []

        'date_now': datetime.date.today(),   # datetime.datetime.now() = June 1, 2023, 9:35 a.m.
        # context['date_now'] = June 1, 2023
        # .html: {{date_now}} = June 1, 2023
        # .html: {{date_now|date:'Y-m-d'}} = 2023-06-01

        'float_number': 1.23456789,
        # context['float_number'] = 1.23456789
        # .html: {{float_number}} = 1.23456789
        # .html: {{float_number|floatformat:2}} = 1.23


        'numbers_list': [1, 2, 3, 4, 5, 6, 7],


        'student_objects_list': [Student('Alex', 18),
                                 Student('Bobby', 19),
                                 Student('Clara', 20)]
    }

    return render(request, template_name, context)


def contact_view(request):
    # return redirect('http://127.0.0.1:8000/')
    return redirect('index')


def about_view(request):
    template_name = 'examples/about.html'
    return render(request, template_name)

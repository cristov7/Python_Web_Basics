from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Employee, Department, Salary

# Create your views here.


def index(request):
    employee = Employee.objects.all()   # Retrieve all objects (lazy - until used, it is not executed)
    # SELECT "web_employee"."id",
    #        "web_employee"."department_id",
    #        "web_employee"."first_name",
    #        "web_employee"."middle_name",
    #        "web_employee"."last_name",
    #        "web_employee"."description",
    #        "web_employee"."age",
    #        "web_employee"."experience",
    #        "web_employee"."birth_date",
    #        "web_employee"."created_on",
    #        "web_employee"."updated_on",
    #        "web_employee"."is_manager",
    #        "web_employee"."email",
    #        "web_employee"."level"
    # FROM "web_employee"
    # LIMIT 21;
    print(employee)
    # <QuerySet [<Employee: ID: 2. Names: Gloria Ivanova>,
    #            <Employee: ID: 1. Names: Peter Petrov>,
    #            <Employee: ID: 3. Names: Georgi Kolev>]>
    print(list(employee))
    # [<Employee: ID: 2. Names: Gloria Ivanova>,
    #  <Employee: ID: 1. Names: Peter Petrov>,
    #  <Employee: ID: 3. Names: Georgi Kolev>]

    departments = Department.objects.all()   # Retrieve all objects (lazy - until used, it is not executed)
    # SELECT "web_department"."id",
    #        "web_department"."name"
    # FROM "web_department"
    # LIMIT 21;
    print(departments)
    # <QuerySet [<Department: 1 IT>]>
    print(list(departments))
    # [<Department: 1 IT>]

    template_name = 'web/index.html'
    context = {
        # Retrieve ALL OBJECTS:
        'employees_objects_all': Employee.objects.all(),   # .all(), .first(), .last()

        # Return OBJECTS that MATCH given parameters:
        'employees_objects_filter': Employee.objects.filter(department_id=1, age__gt=20, age__lt=35),

        # Return OBJECTS that do NOT MATCH given parameters:
        'employees_objects_exclude': Employee.objects.exclude(age=25).order_by('first_name'),

        # Return only ONE OBJECT that MATCHES your query:
        'employee_object_get': Employee.objects.get(age=25),

        # Get the desired OBJECT or raise an HTTP 404 (from django.shortcuts import get_object_or_404):
        'employee_get_object_or_404': get_object_or_404(Employee, first_name='Peter'),

        # Get the desired queryset (casted to LIST) or raise an HTTP 404 (from django.shortcuts import get_list_or_404):
        'employees_get_list_or_404': get_list_or_404(Employee, age__gt=20),

        # To match objects with exactly the given value:
        # - Employee.objects.filter(first_name="Peter")
        # - Employee.objects.exclude(first_name__exact="Peter")   # explicit form ('Peter' == 'Peter')
        # - Employee.objects.get(first_name__iexact="peter")      # case-insensitive match ('pEtEr' == 'Peter')

        # To match objects that contain the given value:
        # - Employee.objects.exclude(first_name__contains="Pet")
        # - Employee.objects.filter(first_name__icontains="pet")   # case-insensitive ('pEt' == 'Pet')

        # To match objects that starts-with or ends-with the given value:
        # - Employee.objects.exclude(first_name__startswith="P")
        # - Employee.objects.filter(first_name__endswith="r")

        # To match objects with a value greater than the given value:
        # - Employee.objects.filter(age__gt=20)    # greater than (age > 20)
        # - Employee.objects.exclude(age_gte=20)   # greater than or equal to (age >= 20)

        # To match objects with a value less than the given value:
        # - Employee.objects.filter(age_lt=20)     # less than (age < 20)
        # - Employee.objects.exclude(age_lte=20)   # less than or equal to (age <= 20)

        # To match objects in a given range (inclusive):
        # - Employee.objects.filter(age__range=(20, 30))   # from 20 to 30 both inclusive (20 <= age <= 30)

        'salary': Salary.objects.filter(amount__gt=1000).first()
    }

    return render(request, template_name, context)


def employee_details(request, pk: int):
    template_name = 'web/details.html'
    context = {'employee': get_object_or_404(Employee, pk=pk)}
    return render(request, template_name, context)


def delete_employee(request, pk: int):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('index')   # (from django.shortcuts import redirect)


# ▪ The 'delete()' method immediately deletes the model object:

    # - Delete a single object:
    # employee = Employee.objects.get(pk=1)
    # employee.delete()

    # - Delete multiple objects in a QuerySet:
    # employees = Employee.objects.all()
    # employees.delete()


def details_department(request, pk: int, slug):
    template_name = 'web/details_department.html'
    context = {'department': get_object_or_404(Department, pk=pk, slug=slug)}
    return render(request, template_name, context)

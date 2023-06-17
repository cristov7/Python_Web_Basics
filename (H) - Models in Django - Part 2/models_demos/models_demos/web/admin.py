from django.contrib import admin
from .models import Employee, NullBlankDemo, Department, Project, Profile, Salary

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    # ModelAdmin Options: add custom options here

    # ▪ Display the model fields:
    list_display = ['pk', 'first_name', 'last_name', 'level']

    # ▪ Add filters to the models:
    list_filter = ['level']

    # ▪ Add search box with field names that will be searched:
    search_fields = ('first_name', 'last_name', 'email')

    # ▪ Make layout changes on "add" and "change" pages:
    # fields = [('first_name', 'last_name'), 'email', 'age', 'level']

    # ▪ Control the layout of "add" and "change" pages:
    fieldsets = [
        ('Personal info',
         {'fields':
             ('first_name', 'middle_name', 'last_name')}
         ),

        ('HR STUFF',
         {'fields':
             ('is_manager', 'email', 'level')}
         )
    ]


@admin.register(NullBlankDemo)
class NullBlankDemoAdmin(admin.ModelAdmin):
    pass


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    pass

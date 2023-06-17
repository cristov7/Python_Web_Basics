from django.db import models
from django.urls import reverse


# Create your models here.

# one class -> one table in the database
# defines structure -> columns / fields and types
# stores data -> from database to python / from python to database
# do operations on database -> python code


class ModifiedMixin(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(models.Model):   # One-to-One Relationship:
    DESK_ONE = 'first'
    DESK_TWO = 'last'
    DESK_CHOICES = (
        (DESK_ONE, 'desk 1'),
        (DESK_TWO, 'desk 2')
    )
    desk = models.CharField(choices=DESK_CHOICES)
    employee = models.OneToOneField('Employee', on_delete=models.CASCADE, primary_key=True)


# class EmployeeProject(models.Model):   # Many-to-Many Relationship
#     employee_id = models.ForeignKey(to='Employee', on_delete=models.CASCADE)
#     project_id = models.ForeignKey(to='Project', on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)


class Project(models.Model):   # Many-to-Many Relationship
    name = models.CharField(max_length=100)


class Department(ModifiedMixin, models.Model):   # Many-to-One Relationship
    name = models.CharField(max_length=50)

    # Add a SlugField
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return f'{self.pk} {self.name}'


class Employee(models.Model):

    # Adding the class is completely optional
    class Meta:
        # Meta options:

        # You can generate a default ordering for the object when retrieving data from the model
        ordering = ['-first_name']   # 'first_name' -> asc; '-first_name' -> desc;

        # You can give a plural name to your model to be represented correctly in the Django admin site:
        verbose_name_plural = 'My Employees'

    # Many-to-One Relationship: class Department
    # models.ForeignKey(to='model / class', on_delete=models.'')
    department = models.ForeignKey(to=Department, on_delete=models.RESTRICT, null=True)
    # CASCADE - if we delete Department, we will delete all connected Employee
    # RESTRICT / PROTECT - if Department has Employee, can't delete Department or Employee
    # SET_NULL - set to null if it is optional

    # Many-to-Many Relationship: class Project, class EmployeeProject
    # models.ManyToManyField('model / class', through='model / class')
    project = models.ManyToManyField(Project)   # through=EmployeeProject

    # One-to-One Relationship: class Profile


    # table + columns

    #   table name -> 'web_employee' == app name 'web' + class name 'employee'
    #   field name -> 'column name' ('first_name' -> 'First name')
    #   field type -> column type ('models.CharField(max_length=30)' -> 'VARCHAR(30)')

    # CharField:
    # - Appropriate for small- to large-sized strings
    # - Has one required argument - max_length
    # verbose_name: convert the column name to name of the field
    # default: A default value or a default callable object for the field
    # blank: False by default. If True, the field is allowed to be blank
    first_name = models.CharField(max_length=30, verbose_name='First name')
    middle_name = models.CharField(max_length=50, default='Doe', blank=True)   # not required because default
    last_name = models.CharField(max_length=40)

    # TextField:
    # - Appropriate for large texts
    description = models.TextField(default='Should be filled in.')   # not required because default

    # IntegerField:
    # - Stores integers
    age = models.IntegerField()   # -5, 0, 100, ...

    # PositiveIntegerField:
    # - Stores integers that could be either positive or zero
    experience = models.PositiveIntegerField()   # starts from 0, 1, 2, ...

    # DateField:
    # - stores a date
    birth_date = models.DateField()   # 1997-03-12

    # DateTimeField:
    # - stores a date and a time
    # auto_now_add: Sets the field to now when the object is first created
    # auto_now: Sets the field to now every time the object is saved
    created_on = models.DateTimeField(auto_now_add=True)   # only first time (on create)
    updated_on = models.DateTimeField(auto_now=True)       # each time update (on update)

    # BooleanField:
    # - Stores Booleans - either True or False
    is_manager = models.BooleanField(default=None)      # not required because default

    # EmailField:
    # - CharField that checks if the value is a valid email address
    # unique: False by default, if True, this field must be unique through the table
    email = models.EmailField(unique=True)

    # choices: It appears as a select box with the created choices instead of a standard text field
    # - Use a sequence consisting of iterables of exactly two items to create choices
    # - A new migration is automatically created each time the list of choices changes
    LEVEL_JUNIOR = 'Jun'
    LEVEL_MIDDLE = 'Mid'
    LEVEL_SENIOR = 'Sen'

    LEVEL_CHOICES = (
        (LEVEL_JUNIOR, 'Junior'),
        (LEVEL_MIDDLE, 'Middle'),
        (LEVEL_SENIOR, 'Senior')
    )
    # value to be set on the model: 'Jun', 'Mid', 'Sen' (save in database)
    # humanreadable name: 'Junior', 'Middle', 'Senior'
    level = models.CharField(max_length=len(LEVEL_SENIOR), choices=LEVEL_CHOICES, default=LEVEL_JUNIOR)
    # not required because default

    # editable:
    # True by default, if False, it modifies the field so:
    # - It is not able to be filled / edited
    # - It disappears from all forms

    @property   # getter
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    # Display the Model Objects:
    # - Use __str__() to return a human-readable representation
    # - In the admin site, in the console, or into a template
    def __str__(self) -> str:
        # 'self.pk' -> id (automatically)
        return f'ID: {self.pk}. Names: {self.full_name}'

    def get_absolute_url(self):
        return reverse('employee_details', kwargs={'pk': self.pk})   # from django.urls import reverse


class NullBlankDemo(models.Model):
    # null - database-related:
    # - False by default. If True, empty values will be stored as NULL
    # - Use for non-string fields such as integers, Booleans, and dates
    # blank - validation-related:
    # - False by default. If True, the field is allowed to be blank

    # can be blank, but can't be null
    blank = models.IntegerField(blank=True, null=False)

    # can't be blank, but can be null
    null = models.IntegerField(blank=False, null=True)

    # can be blank, can be null
    blank_null = models.IntegerField(blank=True, null=True)

    # can't be blank, can't be null
    default = models.IntegerField(blank=False, null=False)


class Salary(models.Model):
    amount = models.PositiveIntegerField()

    def with_taxes_amount(self) -> float:
        return self.amount - (self.amount * 0.2)

    @property   # getter
    def currency(self) -> str:
        return 'USD'

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.with_taxes_amount()} {self.currency}'

    class Meta:
        verbose_name_plural = 'Salaries'

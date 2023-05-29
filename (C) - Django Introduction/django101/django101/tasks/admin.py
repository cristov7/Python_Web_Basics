from django.contrib import admin
from django101.tasks.models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'priority')


admin.site.register(Task, TaskAdmin)

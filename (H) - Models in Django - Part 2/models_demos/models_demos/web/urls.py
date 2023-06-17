from django.urls import path   # , include
from .views import index, delete_employee, employee_details, details_department

urlpatterns = [
    path('', index, name='index'),
    # http://localhost:8000/

    path('delete/<int:pk>/', delete_employee, name='delete'),
    # http://localhost:8000/delete/<int:pk>/

    path('details/<int:pk>', employee_details, name='employee_details'),
    # http://localhost:8000/details/<int:pk>/

    path('dep-details/<int:pk>/<slug:slug>/', details_department, name='details_department')
    # http://localhost:8000/dep-details/<int:pk>/<slug:slug>/
]

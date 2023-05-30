from django.urls import path
from .views import index, details, details_template, details_error

urlpatterns = [
    path('', index),                                           # http://127.0.0.1:8000/departments/

    path('<int:department_id>/', details),                     # http://127.0.0.1:8000/departments/1/

    path('<int:department_id>/', details),                     # http://127.0.0.1:8000/departments/2/

                                                               # http://127.0.0.1:8000/departments/3/

    path('template/<int:department_id>/', details_template),   # http://127.0.0.1:8000/departments/template/1/
                                                               # http://127.0.0.1:8000/departments/template/2/
                                                               # http://127.0.0.1:8000/departments/template/3/

    path('error/<int:department_id>/', details_error)          # http://127.0.0.1:8000/departments/error/1/
                                                               # http://127.0.0.1:8000/departments/error/2/
                                                               # http://127.0.0.1:8000/departments/error/3/
                                                               # http://127.0.0.1:8000/departments/error/4/
]

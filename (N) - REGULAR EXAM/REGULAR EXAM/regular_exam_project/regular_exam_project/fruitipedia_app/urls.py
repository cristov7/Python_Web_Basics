from django.urls import path   # , include
from .views import *

urlpatterns = [
    path('', index_page_func, name='index page'),
    # http://localhost:8000/

    path('dashboard/', dashboard_page_func, name='dashboard page'),
    # http://localhost:8000/dashboard/
]

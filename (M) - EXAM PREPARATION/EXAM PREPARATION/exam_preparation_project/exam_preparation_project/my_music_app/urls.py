from django.urls import path   # , include
from .views import *

urlpatterns = [
    path('', home_page_func, name='home page')
    # http://localhost:8000/
]

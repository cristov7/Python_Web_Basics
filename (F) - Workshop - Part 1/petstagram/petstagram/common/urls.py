from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index')
    # http://127.0.0.1:8000/
]

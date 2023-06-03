from django.urls import path
from .views import index, contact_view, about_view

urlpatterns = [
    path('', index, name='index'),                         # 'http://127.0.0.1:8000/'
    path('contact/', contact_view, name='contact page'),   # 'http://127.0.0.1:8000/contact/'
    path('about/', about_view, name='about page')          # 'http://127.0.0.1:8000/about/'
]

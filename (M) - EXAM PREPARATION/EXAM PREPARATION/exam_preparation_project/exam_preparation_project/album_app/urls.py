from django.urls import path   # , include
from .views import *

urlpatterns = [
    path('add/', add_album_page_func, name='add album page'),
    # http://localhost:8000/album/add/

    path('details/<int:pk>/', album_details_page_func, name='album details page'),
    # http://localhost:8000/album/details/<int:pk>/

    path('edit/<int:pk>/', edit_album_page_func, name='edit album page'),
    # http://localhost:8000/album/edit/<int:pk>/

    path('delete/<int:pk>/', delete_album_page_func, name='delete album page')
    # http://localhost:8000/album/delete/<int:pk>/
]

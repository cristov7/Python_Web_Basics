from django.urls import path   # , include
from .views import *

urlpatterns = [
    path('create/', profile_create_page_func, name='profile create page'),
    # http://localhost:8000/profile/create/

    path('details/', profile_details_page_func, name='profile details page'),
    # http://localhost:8000/profile/details/

    path('edit/', profile_edit_page_func, name='profile edit page'),
    # http://localhost:8000/profile/edit/

    path('delete/', profile_delete_page_func, name='profile delete page'),
    # http://localhost:8000/profile/delete/
]

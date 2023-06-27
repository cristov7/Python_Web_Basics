from django.urls import path   # , include
from .views import *

urlpatterns = [
    path('details/', profile_details_page_func, name='profile details page'),
    # http://localhost:8000/profile/details/

    path('delete/', delete_profile_page_func, name='delete profile page')
    # http://localhost:8000/profile/delete/
]

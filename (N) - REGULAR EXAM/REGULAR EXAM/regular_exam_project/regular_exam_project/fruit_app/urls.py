from django.urls import path   # , include
from .views import *

urlpatterns = [
    path('create/', fruit_create_page_func, name='fruit create page'),
    # http://localhost:8000/create/

    path('<int:pk>/details/', fruit_details_page_func, name='fruit details page'),
    # http://localhost:8000/<int:pk>/details/

    path('<int:pk>/edit/', fruit_edit_page_func, name='fruit edit page'),
    # http://localhost:8000/<int:pk>/edit/

    path('<int:pk>/delete/', fruit_delete_page_func, name='fruit delete page'),
    # http://localhost:8000/<int:pk>/delete/
]

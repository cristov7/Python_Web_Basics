from django.urls import path   # , include
from .views import *

urlpatterns = [
    path('add/', photo_add, name='photo add'),
    # http://127.0.0.1:8000/photos/add/

    path('<int:pk>/', photo_details, name='photo details'),
    # http://127.0.0.1:8000/photos/<int:pk>/

    path('<int:pk>/edit/', photo_edit, name='photo edit'),
    # http://127.0.0.1:8000/photos/<int:pk>/edit/

    path('<int:pk>/delete/', photo_delete, name='photo delete'),
    # http://127.0.0.1:8000/photos/<int:pk>/delete/
]


# urlpatterns = [
#     path('add/', photo_add, name='photo add'),
#     path('<int:pk>/', include([
#         path('', photo_details, name='photo details'),
#         path('edit/', photo_edit, name='photo edit')
#     ]))
# ]

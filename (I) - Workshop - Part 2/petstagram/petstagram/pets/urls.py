from django.urls import path   # , include
from .views import pet_add, pet_details, pet_edit, pet_delete

urlpatterns = [
    path('add/', pet_add, name='pet add'),
    # http://127.0.0.1:8000/pets/add/

    path('<str:username>/pet/<slug:pet_name>/', pet_details, name='pet details'),
    # http://127.0.0.1:8000/pets/<str:username>/pet/<slug:pet_name>/

    path('<str:username>/pet/<slug:pet_name>/edit/', pet_edit, name='pet edit'),
    # http://127.0.0.1:8000/pets/<str:username>/pet/<slug:pet_name>/edit/

    path('<str:username>/pet/<slug:pet_name>/delete/', pet_delete, name='pet delete')
    # http://127.0.0.1:8000/pets/<str:username>/pet/<slug:pet_name>/delete/
]


# urlpatterns = [
#     path('add/', pet_add, name='pet add'),
#     path('<str:username>/pet/<slug:pet_name>/', include([
#         path('', pet_details, name='pet details'),
#         path('edit/', pet_edit, name='pet edit'),
#         path('delete/', pet_delete, name='pet delete')
#     ]))
# ]

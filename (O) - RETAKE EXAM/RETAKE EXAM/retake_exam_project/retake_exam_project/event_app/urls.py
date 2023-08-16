from django.urls import path
from .views import home_func, dashboard_func, create_event_func, event_details_func, edit_event_func, delete_event_func

urlpatterns = [
    path('', home_func, name='home page'),
    # http://localhost:8000/

    path('dashboard/', dashboard_func, name='dashboard page'),
    # http://localhost:8000/dashboard/

    path('create/', create_event_func, name='create event page'),
    # http://localhost:8000/create/

    path('details/<int:pk>/', event_details_func, name='event details page'),
    # http://localhost:8000/details/<int:pk>/

    path('edit/<int:pk>/', edit_event_func, name='edit event page'),
    # http://localhost:8000/edit/<int:pk>/

    path('delete/<int:pk>/', delete_event_func, name='delete event page')
    # http://localhost:8000/delete/<int:pk>/
]

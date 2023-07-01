from django.urls import path   # , include
from .views import *

urlpatterns = [
    path('register/', register_user, name='register user'),
    # http://127.0.0.1:8000/accounts/register/

    path('login/', login_user, name='login user'),
    # http://127.0.0.1:8000/accounts/login/

    path('profile/<int:pk>/', profile_details, name='profile details'),
    # http://127.0.0.1:8000/accounts/profile/<int:pk>/

    path('profile/<int:pk>/edit/', profile_edit, name='profile edit'),
    # http://127.0.0.1:8000/accounts/profile/<int:pk>/edit/

    path('profile/<int:pk>/delete/', profile_delete, name='profile delete')
    # http://127.0.0.1:8000/accounts/profile/<int:pk>/delete/
]


# urlpatterns = [
#     path('register/', register_user, name='register user'),
#     path('login/', login_user, name='login user'),
#     path('profile/<int:pk>/', include([
#         path('', profile_edit, name='profile edit'),
#         path('edit/', profile_edit, name='profile edit'),
#         path('delete/', profile_delete, name='profile delete'),
#     ]))
# ]

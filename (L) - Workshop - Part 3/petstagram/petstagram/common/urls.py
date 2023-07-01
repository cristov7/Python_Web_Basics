from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    # http://127.0.0.1:8000/

    path('like/<int:photo_id>/', like_functionality, name='like'),
    # http://127.0.0.1:8000/like/<int:photo_id>/

    path('share/<int:photo_id>/', share_functionality, name='share'),
    # http://127.0.0.1:8000/share/<int:photo_id>/

    path('comment/<int:photo_id>/', comment_functionality, name='comment')
    # http://127.0.0.1:8000/comment/<int:photo_id>/
]

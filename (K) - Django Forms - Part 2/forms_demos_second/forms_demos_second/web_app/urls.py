from django.urls import path   # , include
from .views import index_func, image_view_func, document_view_func
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', index_func, name='index'),
    # http://localhost:8000/

    path('image/', image_view_func, name='image'),
    # http://localhost:8000/image/

    path('document/', document_view_func, name='document')
    # http://localhost:8000/document/

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Configure the URLs for media

from django.urls import path   # , include
from .views import index_func, model_form_func

urlpatterns = [
    path('', index_func, name='index'),
    # http://localhost:8000/

    path('model-form/<int:pk>/', model_form_func, name='model form')
    # http://localhost:8000/model-form/<int:pk>/
]

"""
URL configuration for regular_exam_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),                                     # http://localhostr:8000/admin/
    path('', include('regular_exam_project.fruit_app.urls')),            # http://localhostr:8000/
    path('', include('regular_exam_project.fruitipedia_app.urls')),      # http://localhostr:8000/
    path('profile/', include('regular_exam_project.profile_app.urls'))   # http://localhostr:8000/profile/
]

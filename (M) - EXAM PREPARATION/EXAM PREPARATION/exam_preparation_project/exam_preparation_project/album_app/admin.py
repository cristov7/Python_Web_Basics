from django.contrib import admin
from exam_preparation_project.album_app.models import *
from exam_preparation_project.profile_app.models import *


@admin.register(AlbumModel)
class AlbumAdmin(admin.ModelAdmin):
    pass


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    pass

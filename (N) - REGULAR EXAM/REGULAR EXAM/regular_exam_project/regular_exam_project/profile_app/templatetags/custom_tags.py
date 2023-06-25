from django import template
from regular_exam_project.profile_app.models import *

register = template.Library()


@register.simple_tag()
def profile_status():
    return ProfileModel.objects.first()

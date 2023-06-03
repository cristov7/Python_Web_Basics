from django import template

register = template.Library()


# simple_tag
@register.simple_tag
def show_student_info(student_obj):
    """"My custom tag"""
    return f"Name: {student_obj.name}, Age: {student_obj.age}"


# 'templatetags.tags': @register.simple_tag
#                      def show_student_info(student_obj):
# '.html': {% for student_obj in students_objects_list %}
#              <p>{% show_student_info student_obj %}</p>
#          {% endfor %}


# 'templatetags.tags': @register.simple_tag(name='info')
# '.html': {% for student_obj in students_objects_list %}#
#              <p>{% info student_obj %}</p>
#          {% endfor %}


# inclusion_tag
@register.inclusion_tag('examples/tags/students_info.html', name='fancy_student', takes_context=True)
# register the tag ---- the path to the html file --------- name for func ------- outer context
def inclusion_student_info(context, student_obj):
    inner_context = {'student_object': student_obj,
                     'score_points': context['float_number']}   # from context: context['float_number'] = 1.23456789
    return inner_context

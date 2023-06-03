from django import template

register = template.Library()


@register.filter(name='odd')
def show_only_odd(value: list):
    """"My custom filter"""
    return [x for x in value if x % 2]


# 'templatetags.filters': @register.filter(name='odd')
# '.html': <p>With odd - custom filter: {{numbers_list|odd}}</p>


# 'templatetags.filters': @register.filter
#                         def show_only_odd(value: list):
# '.html': <p>With odd - custom filter: {{numbers_list|show_only_odd}}</p>

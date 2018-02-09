from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def application_title(value):
    title = ''
    if value:
        title = value
    elif settings.APPLICATION_NAME:
        title = settings.APPLICATION_NAME

    return title

@register.filter
def application_subtitle(value):
    subtitle = ''
    if value:
        subtitle = value
    elif settings.APPLICATION_DESC:
        subtitle = settings.APPLICATION_DESC

    return subtitle


@register.filter
def if_not_exist_in(value,objects):
    result = value
    for o in objects:
        if o.name == value:
            result = ''
    return result

@register.filter
def boolean_icon(value):
    if value:
        return mark_safe('<i class="glyphicon glyphicon-ok"></i>')
    else:
        return mark_safe('<i class="glyphicon glyphicon-remove"></i>')
        

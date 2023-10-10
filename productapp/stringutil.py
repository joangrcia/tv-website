from django import template

register = template.Library()

@register.filter
def ljust(value, arg):
    return str(value).ljust(int(arg))

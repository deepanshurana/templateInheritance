from django import template

register = template.Library()

@register.filter(name='sq')  # decorator
def sq(value):
    return value * value

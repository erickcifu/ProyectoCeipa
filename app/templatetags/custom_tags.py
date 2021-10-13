from  django import template
from random import randint

register = template.Library()

@register.simple_tag(name='set_variable')
def set_variable(valor):
    return valor

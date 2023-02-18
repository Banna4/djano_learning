from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """ this will cut all value of "arg" from yht"""
    return value.replace(arg,'')

#register.filter('cut',cut)
from distutils import extension
import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def sub(value, arg):
    return value - arg


@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))


@register.filter()
def format_date(value):
    result = f'{value.month}월 {value.day}일 {value.hour:0^2}:{value.minute:0^2}'
    return result
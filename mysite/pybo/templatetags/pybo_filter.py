from distutils import extension
import markdown
from django import template
from django.utils.safestring import mark_safe
from django.utils import timezone
from datetime import timedelta

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
    time = timezone.now() - value
    
    if time < timedelta(minutes=1):
        return '방금 전'
    elif time < timedelta(hours=1):
        return str(int(time.seconds / 60)) + '분 전'
    elif time < timedelta(days=1):
        return str(int(time.seconds / 3600)) + '시간 전'
    elif time < timedelta(days=7):
        result = f'{time.days}일 전'
    else:
        result = f'{value.month}월 {value.day}일 {value.hour:0^2}:{value.minute:0^2}'
    return result
from django import template

register = template.Library()

@register.filter(name='split')
def split(value, key):
    """Memecah string menjadi list berdasarkan karakter tertentu"""
    return value.split(key)
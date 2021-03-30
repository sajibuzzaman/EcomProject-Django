from django import template
from ..models import Setting
from Product.models import Category

register = template.Library()

@register.simple_tag
def ecom_cat():
    return Category.objects.all()

@register.simple_tag
def ecom_set():
    return Setting.objects.get(id=1)
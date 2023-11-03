from django import template
from django.db.models import Q

from display_menu.models import Menu, Item

register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(menu_choice):
    items = Item.objects.filter(Q(parent__isnull=True) & Q(menu_id__title=menu_choice))

    return {
        'menu_choice': menu_choice,
        'items': items,
    }
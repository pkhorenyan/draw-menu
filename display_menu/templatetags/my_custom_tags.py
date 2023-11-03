from django import template
from django.db.models import Q

from display_menu.models import Menu, Item

register = template.Library()


@register.simple_tag()
def get_menus():
    return Menu.objects.all()

@register.inclusion_tag('menu.html')
def render_menu(menu_choice):
    items = Item.objects.filter(Q(parent__isnull=True) & Q(menu_id__title=menu_choice))
    # items = Item.objects.filter(menu_id__title=menu_choice, parent__isnull=True)

    return {
        'menu_choice': menu_choice,
        'items': items,
    }
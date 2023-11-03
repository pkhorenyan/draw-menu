from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item, Menu

class ListItemsView(ListView):
    model = Item
    template_name = "home.html"

def get_ancestors(item):
    ancestors = []
    parent = item.parent
    while parent is not None:
        ancestors.insert(0, parent)
        parent = parent.parent
    return ancestors

class ItemDetailView(DetailView):
    model = Item
    template_name = "item.html"

    def get(self, request, item_id):
        selected_item = Item.objects.get(id=item_id)

        selected_item_with_children = Item.objects.filter(Q(id=item_id) | Q(parent=selected_item))

        ancestor_items = get_ancestors(selected_item)
        all_items = Item.objects.all()

        return render(request, 'item.html', {
            'selected_item': selected_item,
            'selected_item_with_children': selected_item_with_children,
            'ancestor_items': ancestor_items,
            'all_items': all_items,
        })

class MenuView(DetailView):
    template_name = "menu.html"

    def get(self, request, menu_name):
        items = Item.objects.filter(Q(parent__isnull=True) & Q(menu_id__title=menu_name))
        return render(request, 'menu.html', {"items": items})

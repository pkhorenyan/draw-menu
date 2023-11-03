from django.views.generic import ListView
from display_menu.models import Item, Menu

class MenuView(ListView):
    model = Menu
    template_name = "draw_menu/draw_menu.html"

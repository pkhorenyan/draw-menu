from django.contrib import admin
from django.urls import path, include
from .views import ListItemsView, ItemDetailView, MenuView

urlpatterns = [
    path('', ListItemsView.as_view(), name="home"),
    path('item/<int:item_id>/', ItemDetailView.as_view(), name="item_detail"),
    path('menu/<str:menu_name>/', MenuView.as_view(), name='menu_view'),
]
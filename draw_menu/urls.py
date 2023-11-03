from django.urls import path, include

from .views import MenuView

urlpatterns = [
    path('<str:menu_name>/', MenuView.as_view(), name='menu_view2'),
]
from django.shortcuts import render
from .models import Menu

def menu_view(request):
    menus = Menu.objects.all()
    return render(request, 'menu_app/menu.html', {'menus': menus})

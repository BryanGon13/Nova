from django.shortcuts import render
from .models import Category, Menu

def menu_view(request):
    categories = Category.objects.all()
    menu_items = Menu.objects.all()
    return render(request, "menu/menu.html", {"categories": categories, "menu_items": menu_items})



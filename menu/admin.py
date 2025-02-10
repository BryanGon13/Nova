from django.contrib import admin

# Register your models here.
from .models import Menu
from .models import Category

# Register with admin
admin.site.register(Menu)
admin.site.register(Category)

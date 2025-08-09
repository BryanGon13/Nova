from django.contrib import admin

# Register your models here.
from .models import Category, Menu

# Register with admin
admin.site.register(Menu)
admin.site.register(Category)

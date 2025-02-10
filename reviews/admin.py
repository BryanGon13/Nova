from django.contrib import admin

# Register your models here.
from .models import Review

# Register with admin
admin.site.register(Review)


from django.contrib import admin

# Register your models here.
from .models import Reservation

# Register with admin
admin.site.register(Reservation)

from django.contrib import admin

# Register your models here.
from .models import About_Us, Awards, Core_Values

# Register with admin
admin.site.register(About_Us)
admin.site.register(Core_Values)
admin.site.register(Awards)

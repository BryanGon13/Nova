from django.contrib import admin

# Register your models here.
from .models import About_Us
from .models import Core_Values
from .models import Awards

# Register with admin
admin.site.register(About_Us)
admin.site.register(Core_Values)
admin.site.register(Awards)



from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Review

@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('title', 'rating', 'created_on')  
    search_fields = ['title']
    list_filter = ('rating',)  
    summernote_fields = ('body',) 





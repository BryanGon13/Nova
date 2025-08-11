# menu/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Menu, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "image_thumb")
    list_filter = ("category",)
    search_fields = ("name", "description")
    readonly_fields = ("image_preview",)
    fields = (
        "category",
        "name",
        "price",
        "description",
        "spiciness_level",
        "vegan",
        "gluten_free",
        "allergens",
        "image_preview",   # shows current image
        "image",           # file picker
    )

    def image_thumb(self, obj):
        if obj.image:
            # small thumbnail in changelist
            return format_html(
                '<img src="{}" style="height:40px; border-radius:6px;" alt="thumb" />',
                obj.image.url,
            )
        return "—"
    image_thumb.short_description = "Image"

    def image_preview(self, obj):
        if obj.image:
            # larger preview on the change form
            return format_html(
                '<img src="{}" style="max-height:160px; border-radius:10px;" alt="preview" />',
                obj.image.url,
            )
        return "No image yet"
    image_preview.short_description = "Current image"
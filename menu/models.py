from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Menu(models.Model):
    SPICE_LEVEL_CHOICES = [
        (0, "Not Spicy 🌿"),
        (1, "Mild 🌶️"),
        (2, "Medium 🌶️🌶️"),
        (3, "Hot 🌶️🌶️🌶️"),
    ]

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="menus", null=True, blank=True
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(max_length=1000)
    spiciness_level = models.IntegerField(choices=SPICE_LEVEL_CHOICES, default=0)
    vegan = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    allergens = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', folder='menu_images')

    def __str__(self):
        return f"[{self.category}] - {self.name}"

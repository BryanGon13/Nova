from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class About_Us(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="aboutus_images/")

    def __str__(self):
        return self.name

class Core_Values(models.Model):
    image = models.ImageField(upload_to="values_images/")
    name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name

class Awards(models.Model):
    organization = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    year_awarded = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="award_images/")

    def __str__(self):
        return self.title

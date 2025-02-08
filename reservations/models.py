from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField()
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()

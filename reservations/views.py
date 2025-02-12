from django.shortcuts import render
from django.views import generic
from .models import Reservation

# Create your views here.

class Booking(generic.ListView):
    model = Reservation
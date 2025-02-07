from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def reservation_home(request):
    return HttpResponse("Welcome to Nova! Please make your reservation here.")
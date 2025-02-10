from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def reservation_home(request):
    return HttpResponse("Customer Reviews")
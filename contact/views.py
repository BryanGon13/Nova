from django.shortcuts import render

def about_us(request):
    return render(request, 'contact/contact.html')  # Ensure this matches the template location

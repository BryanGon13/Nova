from django.urls import path
from . import views

app_name = 'contact'  # This must match the namespace in nova/urls.py

urlpatterns = [
    path('', views.contact_page, name='contact_page'),  # Ensure this is correct
]

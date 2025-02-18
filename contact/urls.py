from django.urls import path
from . import views

app_name = 'contact'  # Namespace must match 'contact' in {% url 'contact:contact' %}

urlpatterns = [
    path('', views.contact_page, name='contact_page'),  # Ensure 'contact_page' is the correct name
]

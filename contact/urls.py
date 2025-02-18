from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us, name='aboutus'),  # URL for the about us page
]

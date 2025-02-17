from django.urls import path
from .views import reservation_list  # Make sure this is the correct import

app_name = 'reservation'  # Ensure this is the correct namespace

urlpatterns = [
    path('', reservation_list, name='reservation_list'),  # Adjust the path as needed
]


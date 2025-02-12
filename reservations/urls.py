from . import views
from django.urls import path

urlpatterns = [
    path('reservation/', views.Booking.as_view(), name='reservation'),
]
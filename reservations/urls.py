from . import views
from django.urls import path


app_name = 'reservation'


urlpatterns = [
    path('reservation/', views.Booking.as_view(), name='reservation'),
]
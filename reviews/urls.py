from django.urls import path
from .views import submit_review


app_name = 'reviews'

urlpatterns = [
    path('', submit_review, name='review_list'),  # Correct view name here
]

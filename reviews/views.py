from django.views.generic import ListView
from .models import Review

class UserReview(ListView):
    model = Review
    template_name = "reviews/reviews.html"  # Ensure it matches your file location
    context_object_name = "review_list"
from django.urls import path
from .views import UserReview

urlpatterns = [
    path("", UserReview.as_view(), name="reviews"),
]

from django.urls import path
from .views import UserReview


app_name = 'review'


urlpatterns = [
    path("", UserReview.as_view(), name="reviews"),
]

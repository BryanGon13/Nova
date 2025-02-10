from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
        
    STAR_RATINGS = [
        (1, "⭐☆☆☆☆"),
        (2, "⭐⭐☆☆☆"),
        (3, "⭐⭐⭐☆☆"),
        (4, "⭐⭐⭐⭐☆"),
        (5, "⭐⭐⭐⭐⭐"),
    ]
    
    # links the review to a user and deletes the review if the user is deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    rating = models.PositiveSmallIntegerField(choices=STAR_RATINGS)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    # to provide a readable string representation when it appears in the Django admin panel
    def __str__(self):
        return f"Review by {self.author} - {self.rating} Stars"

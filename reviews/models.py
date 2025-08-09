from django.contrib.auth.models import User
from django.db import models

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
    title = models.CharField(max_length=100, default="Untitled Review")
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    # posts will now be listed from oldest to newest creation time.
    class Meta:
        ordering = ["-created_on"]

    # now reviews will be displayed in a human.readable manner in the admin panel.
    def __str__(self):
        return f"{self.title} | [written by {self.author}] - [{self.rating} Stars]"

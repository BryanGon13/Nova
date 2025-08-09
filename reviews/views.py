from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ReviewForm
from .models import Review


def review_list(request):
    reviews = Review.objects.all()  # ordered by Meta
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Please log in to post a review.")
            return redirect("account_login")
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            messages.success(request, "Your review was posted.")
            return redirect("reviews:review_list")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = ReviewForm()
    # render your existing template name:
    return render(request, "reviews/reviews.html", {"form": form, "reviews": reviews})


@login_required
def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.author_id != request.user.id:
        messages.error(request, "You can only edit your own review.")
        return redirect("reviews:review_list")

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated.")
            return redirect("reviews:review_list")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = ReviewForm(instance=review)
    return render(request, "reviews/review_form.html", {"form": form, "object": review})


@login_required
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.author_id != request.user.id:
        messages.error(request, "You can only delete your own review.")
        return redirect("reviews:review_list")

    if request.method == "POST":
        review.delete()
        messages.success(request, "Review deleted.")
        return redirect("reviews:review_list")
    return render(request, "reviews/review_confirm_delete.html", {"object": review})

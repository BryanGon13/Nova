from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def review_list(request):
    reviews = Review.objects.all()
    form = ReviewForm()
    return render(request, 'reviews/reviews.html', {'reviews': reviews, 'form': form})
    
    if request.method == "POST" and form.is_valid():
        new_review = form.save(commit=False)
        new_review.author = request.user  # Assign the logged-in user as the review author
        new_review.save()
        return redirect('reviews:review_list')  # Redirect to the same page after saving the review
    
    return render(request, 'reviews.html', {'reviews': reviews, 'form': form})

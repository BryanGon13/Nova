from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def submit_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user  # Set the author automatically
            review.save()
            return redirect('reviews')  # Adjust as needed
    else:
        form = ReviewForm()
    
     # ✅ Fetch reviews to pass to the template
    reviews = Review.objects.all()

    return render(request, 'reviews/reviews.html', {
        'form': form,
        'reviews': reviews
    })

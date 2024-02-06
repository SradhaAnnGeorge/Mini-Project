from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def review(request, billing_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.billing_id = billing_id
            review.save()
            return redirect('review_success')  # Redirect to a success page after submitting the review
    else:
        form = ReviewForm()
    
    return render(request, 'review.html', {'form': form})


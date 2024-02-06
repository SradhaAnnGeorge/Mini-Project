from django.urls import path
from . import views

urlpatterns = [
    # Your other URL patterns
    path('review/<int:billing_id>/', views.review, name='review'),
    path('review/success/', views.review_success, name='review_success'),  # Define a success page URL
]

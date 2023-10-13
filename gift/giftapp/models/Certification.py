from django.db import models
from django.contrib.auth.models import User

class Certification(models.Model):
    APPROVED = 'approved'
    PENDING = 'pending'

    APPROVAL_CHOICES = [
        (APPROVED, 'Approved'),
        (PENDING, 'Pending'),
    ]
   

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    certification_image = models.ImageField(upload_to='certification_image/', null=True, blank=True)
    owner_name = models.CharField(max_length=100)  # Change 'first_name' to 'owner_name'
    is_approved = models.CharField(
        max_length=10,
        choices=APPROVAL_CHOICES,
        default=PENDING,
    )       
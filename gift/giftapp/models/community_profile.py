from django.db import models
from django.contrib.auth.models import User


class Communityprofile(models.Model):
    APPROVED = 'approved'
    PENDING = 'pending'

    APPROVAL_CHOICES = [
        (APPROVED, 'Approved'),
        (PENDING, 'Pending'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,null=True)
    mobile = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True) 
    certification_image = models.ImageField(upload_to='certification_image/', null=True, blank=True)
    is_approval = models.BooleanField(default=False)
    community_is_approved = models.CharField(
        max_length=10,
        choices=APPROVAL_CHOICES,
        default=PENDING,
    )    
    def __str__(self):
        return self.name
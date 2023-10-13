from django.db import models
from django.contrib.auth.models import User


class Communityprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,null=True)
    mobile = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True) 
    is_approval = models.BooleanField(default=False)
    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User  # Import the User model


class Cart(models.Model):
    # Your Cart model fields here
    products = models.ManyToManyField('giftapp.Product', through='giftapp.CartItem')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Allow user to be nullable


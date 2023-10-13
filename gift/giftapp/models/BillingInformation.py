from django.db import models
from django.contrib.auth.models import User
from .product import Product

class BillingInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.TextField()
    town = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    payment_status = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    product = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        if self.user:
            return f"Billing info for {self.name}"
        return "Billing info (No associated user)"

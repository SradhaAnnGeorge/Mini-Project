from django.db import models

class Review(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    rating = models.IntegerField()  # Rating can be a number from 1 to 5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for Product: {self.product.name}"
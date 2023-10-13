from django.db import models
from .category import Category
from .community_profile import Communityprofile
class Product(models.Model):
    community = models.ForeignKey(Communityprofile, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=200, default='1')
    image = models.ImageField(upload_to='products/')

def __str__(self):
        return self.name


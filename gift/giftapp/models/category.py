from django.db import models


class Category(models.Model):
    category_id = models.CharField(max_length=10, unique=True, null=True)
    name = models.CharField(max_length=225, unique=True)


    def __str__(self):
        return self.name

    

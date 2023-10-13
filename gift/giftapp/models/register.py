from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name
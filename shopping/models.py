from django.db import models


# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    discount = models.IntegerField(max_length=100)

    def __str__(self):
        return self.name

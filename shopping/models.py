from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    sizes = (
        ("XS", "Extra Small"),
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("XL", "Extra Large"),
    )
    size = models.CharField(max_length=2, choices=sizes)

    def __str__(self):
        return self.name

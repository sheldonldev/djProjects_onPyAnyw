from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

class Breed(models.Model):
    breed_name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2, "Must longer than 1")]
    )

    def __str__(self):
        return self.breed_name


class Cat(models.Model):
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, null=False)
    cat_name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2, "Must longer than 1")]
    )
    weight = models.FloatField()
    foods = models.CharField(max_length=200)

    def __str__(self):
        return self.cat_name


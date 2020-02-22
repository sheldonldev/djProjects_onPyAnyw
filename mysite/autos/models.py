from django.db import models
from django.core.validators import MinLengthValidator


class MakeUser(models.Model):
    first_name = models.CharField(
        max_length=100,
        help_text='First Name',
        validators=[MinLengthValidator(2, "Must be longer than 1 character")]
    )
    surname = models.CharField(
        max_length=100,
        help_text='Last Name',
        validators=[MinLengthValidator(2, "Must be longer than 1 character")]
    )
    email = models.EmailField()

    def __str__(self):
        return self.email


class AutoUser(models.Model):
    user = models.ForeignKey(MakeUser, on_delete=models.CASCADE, null=False)
    nickname = models.CharField(
        max_length=100,
        help_text="Nick Name",
        validators=[MinLengthValidator(2, "Must be longer than 1 character")]
    )
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)

    def __str__(self):
        return self.nickname

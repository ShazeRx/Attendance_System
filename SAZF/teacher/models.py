from django.db import models
from django.contrib.auth.models import AbstractUser


class Teacher(AbstractUser):
    name=models.CharField(max_length=25)
    surname=models.CharField(max_length=25)
    age=models.IntegerField(null=True)
    age_of_enter=models.DateField(null=True)
    have_class=models.BooleanField(default=False)


from django.db import models
from django.contrib.auth.models import AbstractUser


class Teacher(AbstractUser):
    name=models.CharField(max_length=25)
    surname=models.CharField(max_length=25)
    age=models.IntegerField(max_length=2)
    age_of_enter=models.DateField()
    have_class=models.BooleanField(default=False)


from django.db import models
from django.contrib.auth.models import AbstractUser
import sys
sys.path.append("..")
from student.models import Clas



class Teacher(AbstractUser):
    name=models.CharField(max_length=25)
    surname=models.CharField(max_length=25)
    age=models.IntegerField(null=True)
    age_of_enter=models.DateField(null=True)
    have_class=models.BooleanField(default=False)
    clas=models.OneToOneField(Clas,on_delete=models.CASCADE,related_name='clas_teacher',null=True,blank=True)
    def save(self, *args, **kwargs):
        if self.have_class==True:
            raise ValueError("Insert valid class")
        super().save(*args,**kwargs)



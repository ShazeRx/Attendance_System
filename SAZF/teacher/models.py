from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
import sys
sys.path.append("..")
from student.models import Clas
from .managers import TeacherManager
from django.contrib.auth.models import PermissionsMixin




class Teacher(AbstractBaseUser,PermissionsMixin):
    objects=TeacherManager()
    username=models.CharField(unique=True,max_length=10)
    name=models.CharField(max_length=25)
    surname=models.CharField(max_length=25)
    age=models.IntegerField(null=True)
    age_of_enter=models.DateField(null=True)
    have_class=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    clas=models.OneToOneField(Clas,on_delete=models.CASCADE,related_name='clas_teacher',null=True,blank=True)
    is_admin=models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    profile_photo=models.ImageField(default='profile-default.jpg',null=True)
    USERNAME_FIELD='username'
    REQUIRED_FIELDS = []
    def save(self, *args, **kwargs):
        if self.have_class==True and self.clas==None:
            raise ValueError("Insert valid class")
        super().save(*args,**kwargs)
    def get_full_name(self):
        full_name=self.name + ' ' + self.surname
        return full_name



from django.db import models






class Clas(models.Model):
    name=models.TextField(max_length=3)



class Student(models.Model):
    name=models.CharField(max_length=25)
    surname=models.CharField(max_length=25)
    age=models.IntegerField()
    street=models.CharField(max_length=25)
    building=models.CharField(max_length=4)
    flat=models.IntegerField(null=True,blank=True)
    clas=models.ForeignKey(Clas,on_delete=models.CASCADE,related_name='clas_student')







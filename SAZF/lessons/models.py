from django.db import models
import sys
sys.path.append("..")
from teacher.models import Teacher
from student.models import Clas
lesson_number_choice=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10'),(11,'11')]


class Lesson(models.Model):


    day=[(1,'Monday'),
         (2, 'Tuesday'),
         (3, 'Wednesday'),
         (4, 'Thursday'),
         (5, 'Friday'),
         (6, 'Saturday'),
         (7, 'Sunday')


         ]
    name=models.CharField(max_length=25,null=False,blank=False)
    teacher=models.ForeignKey(Teacher,related_name='teacher',blank=False,null=False,on_delete=models.CASCADE)
    lesson_number=models.IntegerField(choices=lesson_number_choice)
    clas=models.OneToOneField(Clas,on_delete=models.CASCADE,related_name='clas_lesson',blank=False,null=False)
    day_of_week=models.IntegerField(choices=day)
    room=models.IntegerField()








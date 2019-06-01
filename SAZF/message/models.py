from django.db import models
import sys
sys.path.append("..")
from teacher.models import Teacher






class Message(models.Model):
    sender=models.ForeignKey(Teacher, related_name='sender',on_delete=models.CASCADE)
    owner=models.ForeignKey(Teacher,related_name='owner',on_delete=models.CASCADE)
    topic=models.CharField(max_length=25,blank=False,null=False)
    content=models.TextField(null=False,blank=False)
    date=models.DateTimeField(auto_now_add=True)
from django.db import models
import sys
sys.path.append("..")
from teacher.models import Teacher
from django.urls import reverse

class Note(models.Model):
    user=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    #def __str__(self):
        #return str(self.user) + '-' + self.content[0:10] + '...'
    def get_absolute_url(self):
        return reverse('notes')


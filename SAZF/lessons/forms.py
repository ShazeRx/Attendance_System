from django import forms
from .models import Lesson

class LessonCreate(forms.ModelForm):
    class Meta:
        model=Lesson
        fields=['name', 'teacher','clas','room','day_of_week','lesson_number']
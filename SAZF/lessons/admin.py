from django.contrib import admin
from .models import Lesson
from .forms import LessonCreate

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    fields = ('name', 'teacher','clas','room','day_of_week','lesson_number')
    list_display = ('name', 'teacher','clas','room','day_of_week','lesson_number')


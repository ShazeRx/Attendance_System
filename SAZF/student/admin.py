from django.contrib import admin
from .models import Student,Clas
import sys
sys.path.append("..")
from teacher.models import Teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('name', 'surname','age','street','building','flat','clas')
    list_display = ('name','surname','clas')
class StudentsInLine(admin.TabularInline):
    model=Student
class TeacherInLine(admin.StackedInline):
    model = Teacher
@admin.register(Clas)
class ClasAdmin(admin.ModelAdmin):
    inlines = [StudentsInLine,TeacherInLine,]
    fields = ('name',)
    list_display = ('name',)





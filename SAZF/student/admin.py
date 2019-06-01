from django.contrib import admin
from .models import Student,Clas

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('name', 'surname','age','street','building','flat','clas')
    list_display = ('name','surname','clas')
@admin.register(Clas)
class ClasAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)





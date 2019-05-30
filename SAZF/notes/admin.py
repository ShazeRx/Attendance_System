from django.contrib import admin
from .models import Note
from .forms import NoteCreate

@admin.register(Note)
class NotesAdmin(admin.ModelAdmin):
    fields = ('user', 'content')
    list_display = ('user','content')
    form=NoteCreate


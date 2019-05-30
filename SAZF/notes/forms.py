from django.forms import ModelForm
from .models import Note


class NoteCreate(ModelForm):
    class Meta:
        model=Note
        fields=['user','content']
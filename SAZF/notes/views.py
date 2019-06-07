from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Note
from django.views import generic
from django.shortcuts import redirect
import sys
sys.path.append("..")
from teacher.models import Teacher
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
@login_required
def show_notes(request):
    user=request.user


    queryset=Note.objects.filter(user=user)

    return render(request,'notes.html',{'notes':queryset})

class NoteDetail(LoginRequiredMixin,generic.DetailView):
    template_name = 'note_detail.html'
    model = Note

    redirect_field_name = 'redirect_to'

class NoteDelete(LoginRequiredMixin,generic.DeleteView):
    model = Note
    success_url = reverse_lazy('notes')
    template_name = 'note-delete.html'

class NoteUpdate(LoginRequiredMixin,generic.UpdateView):
    model = Note
    template_name = 'note-update.html'
    fields = ['content']
class NoteAdd(LoginRequiredMixin,generic.CreateView):
    model = Note
    template_name = 'note-add.html'
    fields = ['content']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NoteAdd, self).form_valid(form)





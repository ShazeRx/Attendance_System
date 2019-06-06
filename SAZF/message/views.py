from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Message
from django.urls import reverse_lazy,reverse

class ShowMessages(LoginRequiredMixin,generic.ListView):
    template_name = 'message_list.html'
    model = Message

    def get_queryset(self,**kwargs):
        queryset=super(ShowMessages,self).get_queryset()
        user=self.request.user
        queryset=queryset.filter(owner=user)
        print(queryset)
        return queryset








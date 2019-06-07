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
class SendMessage(LoginRequiredMixin,generic.CreateView):
    model = Message
    fields = ['owner','topic','content']
    template_name = 'message_form.html'
    success_url = reverse_lazy('messages')
    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super(SendMessage, self).form_valid(form)
class MessageDetail(LoginRequiredMixin,generic.DetailView):
    model = Message
    template_name = 'message-detail.html'












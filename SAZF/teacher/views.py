from django.shortcuts import render
from .models import Teacher
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Teacher

class ShowTeacherProfile(LoginRequiredMixin,generic.TemplateView):
    template_name = 'profile.html'
    def get_context_data(self, **kwargs):
        context=super(ShowTeacherProfile,self).get_context_data(**kwargs)
        user=self.request.user
        context['profile']=Teacher.objects.filter(username=user)
        return context




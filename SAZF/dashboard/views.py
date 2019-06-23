from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sessions.models import Session
from django.utils import timezone
import sys
sys.path.append("..")
from teacher.models import Teacher

# Create your views here.


def show_dashboard(request):
    def get_current_users():
        active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
        user_id_list = []
        for session in active_sessions:
            data = session.get_decoded()
            user_id_list.append(data.get('_auth_user_id', None))
        # Query all logged in users based on id list
        return Teacher.objects.filter(id__in=user_id_list)



    return render(request,'dashboard.html', {'users':get_current_users().count()})

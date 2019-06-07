from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.


def show_dashboard(request):
    return render(request,'dashboard.html')

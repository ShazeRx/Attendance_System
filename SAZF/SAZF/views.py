from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect


def pagelogout(request):
    if request.method == "POST":
        logout(request)

        return redirect('logout')
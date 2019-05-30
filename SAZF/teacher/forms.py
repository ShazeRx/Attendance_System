from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Teacher

class UserCreateForm(UserCreationForm):
    class Meta:
        model=Teacher
        fields=('username','surname')
class UserChangeeForm(UserChangeForm):
    class Meta:
        model=Teacher
        fields=('username','surname')
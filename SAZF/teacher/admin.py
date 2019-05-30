from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm,UserCreateForm
from .models import Teacher

class CustomUserAdmin(UserAdmin):
    add_form = UserCreateForm
    form = UserChangeForm
    model=Teacher

    list_display = ('username','surname','age','have_class')
admin.site.register(Teacher,CustomUserAdmin)

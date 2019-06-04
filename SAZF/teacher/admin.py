from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm,UserCreateForm
from .models import Teacher

class CustomUserAdmin(UserAdmin):
    add_form = UserCreateForm
    form = UserChangeForm




    list_display = ('username','surname','age','have_class')
    list_filter = ('is_admin',)
    filter_horizontal = ()
    fieldsets = (
        (None, {
            'fields': ('username','surname','age','have_class','age_of_enter','clas')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('is_admin','is_staff','is_active')
        }),
    )



admin.site.register(Teacher,CustomUserAdmin)







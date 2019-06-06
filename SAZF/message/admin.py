from django.contrib import admin
from .models import Message
from .forms import MessageCreateForm

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    fields = ('sender', 'owner','topic','content',)
    list_display = ('sender','owner','topic','date')
    form=MessageCreateForm


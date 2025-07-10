from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender', 'recipient', 'sent_at', 'read')
    list_filter = ('read', 'sent_at')
    search_fields = ('subject', 'body', 'sender__email', 'recipient__email')
    date_hierarchy = 'sent_at'

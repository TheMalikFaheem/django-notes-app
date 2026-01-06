from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'last_modified')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'last_modified')

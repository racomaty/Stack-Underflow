from django.contrib import admin
from .models import *
from accounts.models import *
from chat.models import *

## import all models from all apps

admin.site.register(Biography)
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'date')
    list_filter = ('author', 'date')
    search_fields = ('author', 'text')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message', 'date')
    list_filter = ('sender', 'receiver', 'date')
    search_fields = ('sender', 'receiver', 'message')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'get_tags')
    list_filter = ('author', 'date')
    search_fields = ('title', 'description', 'tags__name')

    def get_tags(self, obj):
        return ', '.join(o for o in obj.tags.names())

# Register your models here.

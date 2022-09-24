from django.contrib import admin
from .models import *
from accounts.models import *
from chat.models import *

## import all models from all apps
admin.site.register(Post)
admin.site.register(Answer)
admin.site.register(Message)

# Register your models here.

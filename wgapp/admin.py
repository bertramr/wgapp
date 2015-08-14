from django.contrib import admin

# Register your models here.

from .models import Flatmate, TaskJournal, TaskList

admin.site.register(Flatmate)
admin.site.register(TaskJournal)
admin.site.register(TaskList)
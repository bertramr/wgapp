from django.contrib import admin

# Register your models here.

from .models import Flatmate, TaskJournal, TaskList, Room

admin.site.register(Flatmate)
admin.site.register(TaskJournal)
admin.site.register(TaskList)
admin.site.register(Room)
from django.contrib import admin

# Register your models here.

from .models import Flatmate, Journal, Task, Room

admin.site.register(Flatmate)
admin.site.register(Journal)
admin.site.register(Task)
admin.site.register(Room)
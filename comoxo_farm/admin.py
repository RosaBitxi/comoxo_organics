from django.contrib import admin
from .models import EditableField, Task, Team, Crop

# Register your models here.
admin.site.register(EditableField)
admin.site.register(Task)
admin.site.register(Team)
admin.site.register(Crop)
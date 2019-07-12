from django.contrib import admin
from AdminManageAPI.models import Asset, Activity, Worker, TaskAssign


# Register your models here.
admin.site.register(Activity)
admin.site.register(Asset)
admin.site.register(Worker)
admin.site.register(TaskAssign)

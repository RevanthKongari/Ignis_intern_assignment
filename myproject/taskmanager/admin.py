# taskmanager/admin.py

from django.contrib import admin
from .models import ScrapingTask

@admin.register(ScrapingTask)
class ScrapingTaskAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'status', 'created_at', 'completed_at')
    search_fields = ('job_id', 'status')

# Register your models here.

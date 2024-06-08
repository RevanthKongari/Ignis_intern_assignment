# taskmanager/models.py

from django.db import models
from django.utils import timezone

class ScrapingTask(models.Model):
    job_id = models.UUIDField(primary_key=True)
    status = models.CharField(max_length=20, default='PENDING')
    created_at = models.DateTimeField(default=timezone.now)
    completed_at = models.DateTimeField(null=True, blank=True)
    result = models.JSONField(null=True, blank=True)

    def __str__(self):
        return str(self.job_id)

from django.db import models
from django.conf import settings


class Experience(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    fromDate = models.DateField(null=True, blank=True)
    toDate = models.DateField(null=True, blank=True)
    i_currently_work_here = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)

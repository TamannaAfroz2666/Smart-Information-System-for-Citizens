from django.db import models
from django.conf import settings


class Skills(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=255, null=True, blank=True)
    skill_level = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)

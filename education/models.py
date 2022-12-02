from django.db import models
from django.conf import settings


class Education(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    board = models.CharField(max_length=255, null=True, blank=True)
    examination = models.CharField(max_length=255, null=True, blank=True)
    roll_no = models.CharField(max_length=255, null=True, blank=True)
    registration_no = models.CharField(max_length=255, null=True, blank=True)
    institution = models.CharField(max_length=255)
    major = models.CharField(max_length=255, null=True, blank=True)
    degree = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    fromDate = models.DateField(null=True, blank=True)
    toDate = models.DateField(null=True, blank=True)
    i_currently_attend = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='education/', null=True, blank=True)

    def __str__(self):
        return str(self.user_id)

from django.db import models
from django.conf import settings


class BirthDayCertificate(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_registration = models.DateField()
    date_of_issue_certificate = models.DateField()
    birth_registration_number = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField(null=True, blank=True)
    birth_place = models.CharField(max_length=300)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    father_nationality = models.CharField(max_length=255)
    mother_nationality = models.CharField(max_length=255)
    present_address = models.CharField(max_length=300)
    is_verified = models.BooleanField(default=False)
    image = models.ImageField(upload_to='birthday_certificate/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)

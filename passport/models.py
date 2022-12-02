from django.db import models
from django.conf import settings
# Create your models here.


class Passport(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # personal data and emergency contact
    name = models.CharField(max_length=255, null=True, blank=True)
    father_name = models.CharField(max_length=255, null=True, blank=True)
    mother_name = models.CharField(max_length=255, null=True, blank=True)
    spouses_name = models.CharField(max_length=255, null=True, blank=True)
    permanent_address = models.CharField(max_length=255, null=True, blank=True)
    # emergency contact
    e_name = models.CharField(max_length=255, null=True, blank=True)
    e_relationship = models.CharField(max_length=255, null=True, blank=True)
    e_address = models.CharField(max_length=255, null=True, blank=True)
    e_phone = models.CharField(max_length=255, null=True, blank=True)
    # passport info
    type = models.CharField(max_length=255, null=True, blank=True)
    country_code = models.CharField(max_length=255, null=True, blank=True)
    passport_number = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    given_name = models.CharField(max_length=255, null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    personal_no = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    previous_passport_no = models.CharField(max_length=255, null=True, blank=True)
    sex = models.CharField(max_length=255, null=True, blank=True)
    place_of_birth = models.CharField(max_length=255, null=True, blank=True)
    date_of_issue = models.DateField(null=True, blank=True)
    issuing_authority = models.CharField(max_length=255, null=True, blank=True)
    date_of_expiry = models.DateField(null=True, blank=True)
    holder_name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='passport/', null=True, blank=True)
    is_verify = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
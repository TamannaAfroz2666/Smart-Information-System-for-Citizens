from django.db import models
from django.conf import settings
# Create your models here.


class NIDInformation(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    professions = models.CharField(max_length=255, null=True, blank=True)
    # name_bangla = models.CharField(max_length=255)
    name_english = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    nid_no = models.CharField(max_length=50)
    back_image = models.ImageField(upload_to='NID_Image_Back/', null=True, blank=True)
    front_image = models.ImageField(upload_to='NID_Image_Front/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.nid_no)

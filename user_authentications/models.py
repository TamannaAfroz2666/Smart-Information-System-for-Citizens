from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.contrib.auth.models import User
from django.conf import settings


class User(AbstractUser):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    is_user = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=12, unique=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(default='image.jpg', null=True, blank=True, upload_to='profile_pics')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

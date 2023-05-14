from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from PIL import Image as PILImage
from io import BytesIO
from django.core.files.base import ContentFile
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    SEX = [
        ('Man', 'Man'),
        ('Woman', 'Woman'),
        ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    phone = PhoneNumberField(blank=True)
    sex = models.CharField(max_length=10, choices=SEX, default=None, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_img/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnail/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.profile_image :
            self.create_thumbnail_100()
        super().save(*args, **kwargs)

    def create_thumbnail_100(self):
        im = PILImage.open(self.profile_image)
        output_size = (200, 200)
        im.thumbnail(output_size)
        thumbnail_io = BytesIO()
        im.save(thumbnail_io, 'JPEG', quality=85)
        thumbnail_io.seek(0)
        self.thumbnail.save(self.profile_image.name, ContentFile(thumbnail_io.read()), save=False)

    def __str__(self):
        return self.username



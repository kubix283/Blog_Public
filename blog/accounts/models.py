from django.db import models
from blog_app.models import Post
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    SEX = [
        ('MAN', 'Man'),
        ('WOMAN', 'Woman'),
        ]
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    sex = models.CharField(max_length=10, choices=SEX, default=None, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_img/', blank=True, null=True)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username



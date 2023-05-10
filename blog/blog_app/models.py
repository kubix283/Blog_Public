from django.db import models
from accounts.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        first_title = self.title.split(' ')
        return ' '.join(first_title[:3])

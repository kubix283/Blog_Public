from django.db import models

class Comment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

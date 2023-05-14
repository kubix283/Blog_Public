from django.db import models
from blog_app.models import Post
from accounts.models import CustomUser

class Comment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="author_comment")

    def __str__(self):
        return self.title

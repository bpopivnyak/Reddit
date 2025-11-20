from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    Title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Comment(models.Model):
    comment = models.ForeignKey(on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to="comments_media/", blank=True, null=True)

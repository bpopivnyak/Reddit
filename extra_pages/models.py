from django.db import models
from accounts.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    about_yourself = models.TextField(null=True, blank=True)
    media = models.FileField(upload_to="comments_media/", blank=True, null=True)

    def __str__(self):
        return self.user.username

class AboutPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

class Notes(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

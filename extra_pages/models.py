from django.db import models
from accounts.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    about_yourself = models.TextField()
    media = models.FileField(upload_to="comments_media/", blank=True, null=True)

    def __str__(self):
        return self.user


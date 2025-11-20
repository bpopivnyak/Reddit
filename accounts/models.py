from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=255)
    permissions = models.ManyToManyField("auth.Permission")

    def __str__(self):
        return self.name

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to="user_image")
    description = models.CharField(max_length=255, blank=True, null=True)
    rules = models.TextField(blank=True, null=True)


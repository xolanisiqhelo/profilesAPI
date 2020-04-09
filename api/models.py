from django.db import models
from django.contrib.auth.models import User


class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    related_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    poster = models.ForeignKey(User, on_delete=models.PROTECT, related_name="uploadedPosts")
    text = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, blank=True)

class UserFollowing(models.Model):
    user_id = models.ForeignKey("User", related_name="following")
    following_user_id = models.ForeignKey("User", related_name="followers")

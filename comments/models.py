from django.contrib.auth.models import User
from django.db import models

from posts.models import Post


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Post")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)

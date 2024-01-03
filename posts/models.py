from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    date_created = models.DateTimeField(auto_now_add=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']

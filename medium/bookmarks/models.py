from django.db import models
from django.contrib.auth.models import User
from blog.models import Blog

# Create your models here.
class Bookmark(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    bookmark_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.post.title}"

   
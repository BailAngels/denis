from django.db import models
from django.contrib.auth import get_user_model

from apps.blogs.models import Blog
User = get_user_model()


class Comment(models.Model):
    text = models.TextField(
        verbose_name='Комент',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.username
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
        related_name='comments'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='com_p'
    )
    def __str__(self):
        return self.user.username
    

class CommentLike(models.Model):
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='comment_like'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.username

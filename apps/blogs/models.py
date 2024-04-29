from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Blog(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор',
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Название',
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    image = models.ImageField(
        upload_to='blog/',
        verbose_name='Изображение',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания',
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'


class BlogLike(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='blog_like',
        verbose_name='блог',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь',
    )

    def __str__(self):
        return self.blog.title
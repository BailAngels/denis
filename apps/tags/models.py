from django.db import models

from apps.blogs.models import Blog

class Tag(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Название тега',
    )
    blog=models.ManyToManyField(
        Blog,
        related_name='tag',
        verbose_name='Cвязь блогам',
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Тег'
        verbose_name_plural='Теги'
        



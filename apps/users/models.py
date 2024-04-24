from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nick = models.CharField(
        max_length=50,
        verbose_name='Никнейм',
    )
    avatar = models.ImageField(
        upload_to='user/',
        verbose_name='Аватарка',
    )
    bio = models.TextField(
        verbose_name='Биография',
    )

    def __str__(self):
        return self.nick
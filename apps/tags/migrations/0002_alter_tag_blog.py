# Generated by Django 5.0.4 on 2024-04-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='blog',
            field=models.ManyToManyField(related_name='tags', to='blogs.blog', verbose_name='Cвязь блогам'),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-10 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_post_delete_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='опубликовано'),
        ),
        migrations.AddField(
            model_name='post',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='post',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='просмотры'),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-12 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, max_length=100, null=True, verbose_name='Содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение')),
                ('date_start', models.DateTimeField(blank=True, null=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('views_count', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'посты',
            },
        ),
    ]

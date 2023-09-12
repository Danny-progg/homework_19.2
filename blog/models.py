from django.db import models

NUllABLE = {'blank': True, 'null': True}

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок', **NUllABLE)
    slug = models.CharField(max_length=100, verbose_name='slug', **NUllABLE),
    content = models.TextField(max_length=100, verbose_name='Содержимое', **NUllABLE)
    preview = models.ImageField(upload_to='images/', verbose_name='Изображение', **NUllABLE)
    date_start = models.DateTimeField(verbose_name='Дата создания', **NUllABLE)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.title} - {self.content}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

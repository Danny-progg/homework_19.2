from django.db import models

NUllABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', **NUllABLE)
    description = models.CharField(max_length=100, verbose_name='Описание', **NUllABLE)

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', **NUllABLE)
    description = models.TextField(max_length=100, verbose_name='Описание', **NUllABLE)
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', **NUllABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name="Цена")
    date_start = models.DateTimeField(verbose_name='Дата создания', **NUllABLE)
    data_end = models.DateTimeField(verbose_name="Дата закрытия", **NUllABLE)

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
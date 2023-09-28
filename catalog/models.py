from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name='Наименование', **NULLABLE)
    description = models.CharField(max_length=100, verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', **NULLABLE)
    description = models.TextField(max_length=100, verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name="Цена")
    date_start = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    data_end = models.DateTimeField(verbose_name="Дата закрытия", **NULLABLE)

    vendor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='продавец')

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    objects = None
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Название версии', **NULLABLE)
    version_sign = models.BooleanField(default=True, verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.product}.'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    Product.objects.all().delete()
    Category.objects.all().delete()

    def handle(self, *args, **options):
        categories_list = [{'id': 1, 'name': 'fruit', 'description': 'fruity'},
                           {'id': 2, 'name': 'vegetable', 'description': 'vegetable'}]

        products_list = [{'name': 'orange', 'description': 'orange', 'category_id': 1, 'price': 13},
                         {'name': 'apple', 'description': 'apple', 'category_id': 1, 'price': 21}]

        for item in categories_list:
            Category.objects.create(**item)

        for item in products_list:
            Product.objects.create(**item)
from django.shortcuts import render
from catalog.models import Product


def index(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def products(request):
    products_list = Product.objects.all()[:1]
    context = {
        'object_list': products_list,
        'title': 'Продукты'
    }
    return render(request, 'catalog/products.html', context)


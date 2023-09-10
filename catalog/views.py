from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Product, Category


def index(request):
    products_list = Category.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/index.html', context)


class ContactListView(ListView):
    model = Product
    extra_context = {
        'title': 'Контакты'
    }
    template_name = 'catalog/contact_list.html'


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Продукты'
    }
    template_name = 'catalog/product_list.html'



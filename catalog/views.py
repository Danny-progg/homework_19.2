from django.shortcuts import render
from django.views.generic import ListView
from catalog.models import Product, Category


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории',
    }
    template_name = 'catalog/category_list.html'


class BlogListView(ListView):
    model = Product
    extra_context = {
        'title': 'Блог'
    }
    template_name = 'catalog/blog_list.html'


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Продукты'
    }
    template_name = 'catalog/product_list.html'


class SpecificListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'Категория: {category_item.name}'

        return context_data

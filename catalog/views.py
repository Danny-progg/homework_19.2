from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from catalog.models import Product, Category, Post


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории',
    }
    template_name = 'catalog/category_list.html'


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


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content',)
    success_url = reverse_lazy('catalog:post_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content',)
    success_url = reverse_lazy('catalog:post_list')


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('catalog:post_list')


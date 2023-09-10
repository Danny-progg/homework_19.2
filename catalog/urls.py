from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import BlogListView, CategoryListView, ProductListView, SpecificListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/specific/', SpecificListView.as_view(), name='spec_category_list')
]
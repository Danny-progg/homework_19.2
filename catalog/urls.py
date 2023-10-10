from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import (ProductListView, SpecificListView, ProductDeleteView, ProductDetailView,
                           ProductCreateView, ProductUpdateView, categories)

app_name = CatalogConfig.name

urlpatterns = [
    # path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/', categories, name='category_list'),
    path('', cache_page(60)(ProductListView.as_view()), name='product_list'),
    path('<int:pk>/specific/', SpecificListView.as_view(), name='spec_category_list'),
    path('create/', never_cache(ProductCreateView.as_view()), name='product_form'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_update_form'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_confirm_delete'),
]

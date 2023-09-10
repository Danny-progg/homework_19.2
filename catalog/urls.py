from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (CategoryListView, ProductListView, SpecificListView, PostCreateView, PostListView,
                           PostDetailView, PostUpdateView, PostDeleteView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/specific/', SpecificListView.as_view(), name='spec_category_list'),
    path('create/', PostCreateView.as_view(), name='post_form'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('view/<int:pk>/', PostDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
]

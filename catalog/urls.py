from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (CategoryListView, ProductListView, SpecificListView, ProductDeleteView, ProductDetailView,
                           ProductCreateView, ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/specific/', SpecificListView.as_view(), name='spec_category_list'),

    path('create/', ProductCreateView.as_view(), name='product_form'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_update_form'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_confirm_delete'),
]

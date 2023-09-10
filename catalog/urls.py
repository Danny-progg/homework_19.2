from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ContactListView, index, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', ContactListView.as_view(), name='contact_list'),
    path('products/', ProductListView.as_view(), name='product_list')
]
from django.urls import path
from django.views.decorators.cache import never_cache

from blog.apps import BlogConfig
from blog.views import (PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView)

app_name = BlogConfig.name

urlpatterns = [
    path('create/', never_cache(PostCreateView.as_view()), name='post_form'),
    path('', PostListView.as_view(), name='post_list'),
    path('view/<int:pk>/', PostDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
]
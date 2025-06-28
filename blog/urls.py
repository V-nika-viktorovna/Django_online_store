from django.urls import path

from blog.apps import BlogConfig
from blog.views import (BlogContactsView, BlogCreateView, BlogDeleteView,
                        BlogDetailView, BlogListView, BlogUpdateView)

app_name = BlogConfig.name

urlpatterns = [
    path('home/article', BlogListView.as_view(), name='home_article'),
    path('contacts/article', BlogContactsView.as_view(), name='contacts_article'),
    path('article_info/<int:pk>/', BlogDetailView.as_view(), name='article_info'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/updata/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete')
]

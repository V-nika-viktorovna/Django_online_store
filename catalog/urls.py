from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts_view, home_view, product_info_view

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home_view, name='home'),
    path('contacts/', contacts_view, name='contacts'),
    path('product_info/<int:pk>/', product_info_view, name='product_info'),
    path('product_info/<int:pk>/', product_info_view, name='product_info'),
]

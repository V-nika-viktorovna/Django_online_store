from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (CatalogContactsViev, CatalogCreateView,
                           CatalogDeleteView, CatalogDetailViev,
                           CatalogListViev, CatalogUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', CatalogListViev.as_view(), name='home'),
    path('contacts/', CatalogContactsViev.as_view(), name='contacts'),
    path('product_info/<int:pk>/', CatalogDetailViev.as_view(), name='product_info'),
    path('product/create/', CatalogCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', CatalogUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', CatalogDeleteView.as_view(), name='product_delete'),
]

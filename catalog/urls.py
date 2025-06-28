from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (CatalogContactsViev, CatalogDetailViev,
                           CatalogListViev)

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', CatalogListViev.as_view(), name='home'),
    path('contacts/', CatalogContactsViev.as_view(), name='contacts'),
    path('product_info/<int:pk>/', CatalogDetailViev.as_view(), name='product_info'),
]
